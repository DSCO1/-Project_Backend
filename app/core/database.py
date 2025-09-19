from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# This is the connection URL for our PostgreSQL database running in Docker.
# It matches the details in our docker-compose.yml file.
SQLALCHEMY_DATABASE_URL = "postgresql://myuser:mypassword@localhost/career_advisor"

# The 'engine' is the entry point to our database.
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Each instance of the SessionLocal class will be a new database session.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# This is a base class that our model classes will inherit from.
Base = declarative_base()