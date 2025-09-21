from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app import models, schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users/", response_model=schemas.User)
def create_or_update_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    Creates a new user or updates an existing user's details.
    """
    db_user = db.query(models.User).filter(models.User.id == user.id).first()
    
    if db_user:
        # --- CORRECTED UPDATE LOGIC ---
        # Update all fields from the incoming data
        db_user.name = user.name
        db_user.current_education_level = user.current_education_level
        db_user.stream = user.stream
        db_user.academic_marks = user.academic_marks
        db_user.location = user.location
    else:
        # --- CORRECTED CREATE LOGIC ---
        # Create a new user with all fields from the input schema
        db_user = models.User(**user.model_dump())
        db.add(db_user)
        
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/users/{user_id}", response_model=schemas.User)
def get_user_details(user_id: str, db: Session = Depends(get_db)):
    """
    Retrieves the details for a specific user by their ID.
    """
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user