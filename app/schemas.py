from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

# --- Helper Schema ---
class CareerForSkill(BaseModel):
    id: int
    name: str
    model_config = ConfigDict(from_attributes=True)

# --- Main Schemas ---
class Skill(BaseModel):
    id: int
    name: str
    careers: List[CareerForSkill] = []
    model_config = ConfigDict(from_attributes=True)

class Course(BaseModel):
    name: str
    stream: str
    duration_years: int
    model_config = ConfigDict(from_attributes=True)

class College(BaseModel):
    id: int
    name: str
    location: str
    courses: List[Course] = []
    model_config = ConfigDict(from_attributes=True)

class Career(BaseModel):
    id: int
    name: str
    description: str | None = None
    skills: List[Skill] = []
    model_config = ConfigDict(from_attributes=True)
    
# --- UPDATED USER SCHEMAS ---
class UserBase(BaseModel):
    name: str | None = None
    current_education_level: str | None = None
    stream: str | None = None
    academic_marks: float | None = None
    location: str | None = None

class UserCreate(UserBase):
    id: str # The Firebase UID from the app

class User(UserBase):
    id: str
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)