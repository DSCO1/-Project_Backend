from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

# --- Helper Schemas ---
class CareerForSkill(BaseModel):
    id: int
    name: str
    model_config = ConfigDict(from_attributes=True)

class CollegeForCourse(BaseModel):
    id: int
    name: str
    location: str
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
    colleges: List[CollegeForCourse] = [] # <-- ADDED THIS
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
    courses: List[Course] = []
    model_config = ConfigDict(from_attributes=True)
    
class UserBase(BaseModel):
    name: str | None = None
    current_education_level: str | None = None
    stream: str | None = None
    academic_marks: float | None = None
    location: str | None = None

class UserCreate(UserBase):
    id: str

class User(UserBase):
    id: str
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

# Add this new class to your schemas.py file

class QuizAnswers(BaseModel):
    q1: str
    q2: str | None = None
    q3: str | None = None
    q4: str | None = None
    q5: str | None = None