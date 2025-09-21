import pandas as pd
from app.core.database import SessionLocal
from app.models.career import Career
from app.models.skill import Skill
from app.models.college import College
from app.models.course import Course
from app.models.associations import career_skill_association, college_course_association

def seed_data():
    """
    Reads all CSV files, seeds primary tables, and creates relationships
    based on mapping CSVs. This is the definitive seeder.
    """
    db = SessionLocal()
    
    try:
        # --- 1. SEED PRIMARY TABLES ---
        
        # Seed Careers
        if db.query(Career).count() == 0:
            df = pd.read_csv('careers_data.csv')
            for _, row in df.iterrows(): db.add(Career(name=row['name'], description=row['description']))
            db.commit()
            print("Careers seeded.")
        
        # Seed Skills
        if db.query(Skill).count() == 0:
            df = pd.read_csv('skills_data.csv')
            for _, row in df.iterrows(): db.add(Skill(name=row['name']))
            db.commit()
            print("Skills seeded.")

        # Seed Colleges
        if db.query(College).count() == 0:
            df = pd.read_csv('colleges_data.csv')
            for _, row in df.iterrows(): db.add(College(name=row['name'], location=row['location']))
            db.commit()
            print("Colleges seeded.")

        # Seed Courses
        if db.query(Course).count() == 0:
            df = pd.read_csv('courses_data.csv')
            for _, row in df.iterrows(): db.add(Course(name=row['name'], stream=row['stream'], duration_years=row['duration_years']))
            db.commit()
            print("Courses seeded.")

        print("Primary data tables are populated.")

        # --- 2. CREATE RELATIONSHIPS ---

        # Create Career-Skill links
        if db.query(career_skill_association).count() == 0:
            print("Creating career-skill relationships...")
            df_map = pd.read_csv('career_skills_map.csv')
            for _, row in df_map.iterrows():
                career_obj = db.query(Career).filter_by(name=row['career_name']).first()
                skill_obj = db.query(Skill).filter_by(name=row['skill_name']).first()
                if career_obj and skill_obj:
                    career_obj.skills.append(skill_obj)
            db.commit()
            print("Career-skill relationships created.")
        else:
            print("Career-skill relationships already exist.")
        
        # Create College-Course links
        if db.query(college_course_association).count() == 0:
            print("Creating college-course relationships...")
            df_map = pd.read_csv('college_courses_map.csv')
            for _, row in df_map.iterrows():
                college_obj = db.query(College).filter_by(name=row['college_name']).first()
                course_obj = db.query(Course).filter_by(name=row['course_name']).first()
                if college_obj and course_obj:
                    college_obj.courses.append(course_obj)
            db.commit()
            print("College-course relationships created.")
        else:
            print("College-course relationships already exist.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_data()