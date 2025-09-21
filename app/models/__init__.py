from ..core.database import Base

# Import all the models so that Base has them registered
from .user import User
from .career import Career
from .skill import Skill
from .course import Course
from .college import College
from .associations import career_skill_association, college_course_association