from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.database import SessionLocal
from app.services.recommendation_service import RecommendationService
from app import schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users/{user_id}/recommendations/", response_model=List[schemas.Career])
def get_career_recommendations(user_id: str, quiz_answers: schemas.QuizAnswers, db: Session = Depends(get_db)):
    """
    Accepts quiz answers for a specific user and returns personalized 
    career recommendations with associated skills and courses.
    """
    print(f"--- Received recommendation request for user: {user_id} ---")
    print(f"Received quiz answers: {quiz_answers.model_dump()}")

    service = RecommendationService(db_session=db)
    recommendations = service.get_recommendations(user_id=user_id, quiz_answers=quiz_answers.model_dump())
    
    if recommendations and "error" in recommendations[0]:
         raise HTTPException(status_code=404, detail=recommendations[0]["error"])

    print(f"--- Found {len(recommendations)} recommendations. Sending response. ---")
    return recommendations