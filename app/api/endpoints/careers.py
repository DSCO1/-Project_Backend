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

@router.get("/careers/", response_model=List[schemas.Career])
def get_all_careers(db: Session = Depends(get_db)):
    """
    Returns a list of all careers and their associated skills.
    """
    careers = db.query(models.Career).all()
    return careers