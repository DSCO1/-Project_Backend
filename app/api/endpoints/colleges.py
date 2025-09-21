from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.core.database import SessionLocal
from app import models, schemas # <-- CORRECTED THIS LINE

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/colleges/", response_model=List[schemas.College])
def get_all_colleges(db: Session = Depends(get_db)):
    """
    Returns a list of all colleges and the courses they offer.
    """
    colleges = db.query(models.College).all()
    return colleges