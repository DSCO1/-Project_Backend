from sqlalchemy.orm import Session, joinedload
from collections import Counter
from .. import models

class RecommendationService:
    def __init__(self, db_session: Session):
        self.db = db_session

    def get_recommendations(self, user_id: str, quiz_answers: dict) -> list:
        # Step 1: Fetch the User's Full Profile
        user = self.db.query(models.User).filter(models.User.id == user_id).first()
        if not user or not user.stream:
            # Cannot give academic recommendations without a stream
            return []

        # Step 2: Determine Primary Trait from Quiz
        user.quiz_answers = quiz_answers
        self.db.commit()
        trait_scores = Counter(quiz_answers.values())
        primary_trait = trait_scores.most_common(1)[0][0] if trait_scores else None
        if not primary_trait:
            return []

        # Step 3: Initial Career Filtering based on Trait
        trait_to_career_map = {
            "Analytical": ["Software Developer", "Data Scientist", "Civil Engineer", "Chartered Accountant"],
            "Creative": ["Graphic Designer", "UI/UX Designer", "Content Writer / Copywriter", "Architect"],
            "Social": ["Doctor (General Physician)", "Teacher / Professor", "Lawyer", "Social Worker"]
        }
        career_names = trait_to_career_map.get(primary_trait, [])
        
        # Step 4: Find careers that match the trait AND the user's academic stream.
        # We use joinedload to pre-fetch all the related data in one efficient query.
        recommended_careers = self.db.query(models.Career).options(
            joinedload(models.Career.skills),
            joinedload(models.Career.courses).joinedload(models.Course.colleges)
        ).filter(
            models.Career.name.in_(career_names),
            models.Career.courses.any(models.Course.stream == user.stream)
        ).all()

        # Step 5 (Optional but good): Prioritize local colleges in the results
        for career in recommended_careers:
            for course in career.courses:
                # Sort colleges for this course, putting local ones first
                course.colleges.sort(key=lambda college: college.location != user.location)

        return recommended_careers