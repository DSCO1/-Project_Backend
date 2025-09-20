# We import the 'Base' and 'engine' we defined in our database connector.
from app.core.database import Base, engine

# It's crucial to import all your models here so that SQLAlchemy knows about them.
from app.models.career import Career
from app.models.user import User
from app.models.skill import Skill
from app.models.associations import career_skill_association
from app.models.course import Course # <-- ADD THIS LINE
from app.models.college import College # <-- ADD THIS LINE

print("Connecting to the database and creating tables...")

# This magic line creates all tables that inherit from 'Base'.
Base.metadata.create_all(bind=engine)

print("Tables created successfully.")