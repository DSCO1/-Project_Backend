from sqlalchemy import Column, Integer, String, Text
from ..core.database import Base # We import the Base from our database file

# This class defines the 'careers' table in our database.
class Career(Base):
    __tablename__ = "careers"

    # These are the columns in our table.
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(Text, nullable=True)
    avg_salary = Column(String, nullable=True)
    source = Column(String, default="curated")

