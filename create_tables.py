from app.core.database import Base, engine

# Import all our models and associations
from app.models.career import Career
from app.models.user import User
from app.models.skill import Skill
from app.models.course import Course
from app.models.college import College
from app.models.associations import career_skill_association, college_course_association # <-- UPDATE THIS LINE

print("Connecting to the database and creating tables...")

Base.metadata.create_all(bind=engine)

print("Tables created successfully.")