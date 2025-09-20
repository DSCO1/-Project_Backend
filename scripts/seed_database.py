import pandas as pd
from app.core.database import SessionLocal
from app.models.career import Career
from app.models.skill import Skill
from app.models.college import College
from app.models.course import Course

def seed_data():
    """
    Reads all primary data CSV files and seeds the database tables if they are empty.
    """
    db = SessionLocal()
    
    try:
        # --- Seed Careers ---
        if db.query(Career).count() == 0:
            print("Seeding careers...")
            df = pd.read_csv('careers_data.csv')
            for index, row in df.iterrows():
                db.add(Career(name=row['name'], description=row['description']))
            db.commit()
            print("Careers seeded successfully.")
        else:
            print("Careers table is not empty. Skipping.")

        # --- Seed Skills ---
        if db.query(Skill).count() == 0:
            print("Seeding skills...")
            df = pd.read_csv('skills_data.csv')
            for index, row in df.iterrows():
                db.add(Skill(name=row['name']))
            db.commit()
            print("Skills seeded successfully.")
        else:
            print("Skills table is not empty. Skipping.")

        # --- Seed Colleges ---
        if db.query(College).count() == 0:
            print("Seeding colleges...")
            df = pd.read_csv('colleges_data.csv')
            for index, row in df.iterrows():
                db.add(College(name=row['name'], location=row['location']))
            db.commit()
            print("Colleges seeded successfully.")
        else:
            print("Colleges table is not empty. Skipping.")

        # --- Seed Courses ---
        if db.query(Course).count() == 0:
            print("Seeding courses...")
            df = pd.read_csv('courses_data.csv')
            for index, row in df.iterrows():
                db.add(Course(name=row['name'], stream=row['stream'], duration_years=row['duration_years']))
            db.commit()
            print("Courses seeded successfully.")
        else:
            print("Courses table is not empty. Skipping.")

    except FileNotFoundError as e:
        print(f"Error: A required CSV file was not found. {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_data()