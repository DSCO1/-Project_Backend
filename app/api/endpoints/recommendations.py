from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
# CHANGED: We now import from 'app' directly.
from app.core.database import SessionLocal
from app.services.recommendation_service import RecommendationService

# Create a router to group related endpoints
router = APIRouter()

# Dependency to get a DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/recommendations/")
def get_career_recommendations(quiz_answers: dict, db: Session = Depends(get_db)):
    """
    Accepts quiz answers and returns personalized career recommendations.
    """
    # Create an instance of our service
    service = RecommendationService(db_session=db)
    
    # Call the method we just built
    recommendations = service.get_recommendations(quiz_answers)
    
    return recommendations