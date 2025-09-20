from sqlalchemy.orm import Session
from collections import Counter
from .. import models

class RecommendationService:
    def __init__(self, db_session: Session):
        self.db = db_session

    def get_recommendations(self, quiz_answers: dict) -> list:
        """
        Takes a dictionary of quiz answers and returns a list of
        personalized career recommendations.
        """
        print("Received quiz answers:", quiz_answers)
        
        # --- Step 1: Analyze quiz answers ---
        # We assume the quiz answers provide tags like 'Analytical', 'Creative', etc.
        
        # Use a Counter to easily count the occurrences of each trait
        trait_scores = Counter(quiz_answers.values())
        
        print("Calculated trait scores:", trait_scores)

        # Get the highest scoring trait. If there's a tie, it picks one.
        primary_trait = trait_scores.most_common(1)[0][0] if trait_scores else None
        
        if not primary_trait:
            return [{"message": "Could not determine primary trait from answers."}]

        print(f"User's primary trait is: {primary_trait}")

        # --- LOGIC TO BE BUILT NEXT ---
        # Step 2: Create a scoring system for careers based on this primary_trait.
        # Step 3: Filter and rank careers.
        # Step 4: Find associated courses and colleges.

        # For now, let's return a placeholder with our findings.
        recommendations = [
            {"message": f"Recommendation logic for the '{primary_trait}' trait is not yet implemented."}
        ]
        
        return recommendations