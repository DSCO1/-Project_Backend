from sqlalchemy.orm import Session, joinedload
from collections import Counter
from .. import models

class RecommendationService:
    def __init__(self, db_session: Session):
        self.db = db_session

    def get_recommendations(self, user_id: str, quiz_answers: dict) -> list:
        """
        Generates personalized recommendations based on a user's full profile
        and quiz answers.
        """
        # --- Step 1: Fetch the User's Full Profile ---
        user = self.db.query(models.User).filter(models.User.id == user_id).first()
        if not user:
            return [{"error": "User not found"}]

        # Save the latest quiz answers to the user's profile
        user.quiz_answers = quiz_answers
        self.db.commit()

        # --- Step 2: Determine Primary Trait from Quiz ---
        trait_scores = Counter(quiz_answers.values())
        primary_trait = trait_scores.most_common(1)[0][0] if trait_scores else None
        if not primary_trait:
            return []

        print(f"User Profile: Trait='{primary_trait}', Stream='{user.stream}', Location='{user.location}'")

        # --- Step 3: Initial Career Filtering based on Trait ---
        # In a real app, this map would be in the database, but this is fine for our project.
        trait_to_career_map = {
            "Analytical": ["Software Developer", "Data Scientist", "Civil Engineer", "Chartered Accountant"],
            "Creative": ["Graphic Designer", "UI/UX Designer", "Content Writer / Copywriter", "Architect"],
            "Social": ["Doctor (General Physician)", "Teacher / Professor", "Lawyer", "Social Worker"]
        }
        career_names = trait_to_career_map.get(primary_trait, [])
        
        # --- Step 4: Multi-level Filtering and Data Assembly ---
        
        # Find career objects that also have courses matching the user's stream
        recommended_careers = self.db.query(models.Career).options(
            joinedload(models.Career.skills), # Pre-load skills
            joinedload(models.Career.courses).joinedload(models.Course.colleges) # Pre-load courses and their colleges
        ).filter(
            models.Career.name.in_(career_names),
            models.Career.courses.any(models.Course.stream == user.stream)
        ).all()

        return recommended_careers