# We import the 'Base' and 'engine' we defined in our database connector.
from app.core.database import Base, engine

# It's crucial to import all your models here so that SQLAlchemy knows about them.
from app.models.career import Career 

print("Connecting to the database and creating tables...")

# This is the magic line.
# It checks all the classes that inherit from 'Base' and creates
# the corresponding tables in the database.
Base.metadata.create_all(bind=engine)

print("Tables created successfully.")