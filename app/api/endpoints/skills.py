from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.core.database import SessionLocal
from app import models, schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/skills/", response_model=List[schemas.Skill])
def get_all_skills(db: Session = Depends(get_db)):
    """
    Returns a list of all skills and the careers they are associated with.
    """
    skills = db.query(models.Skill).all()
    return skills