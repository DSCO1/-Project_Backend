import pandas as pd
from app.core.database import SessionLocal
from app.models import Career, Skill, College, Course
from app.models.associations import career_skill_association, college_course_association, career_course_association

def seed_data():
    db = SessionLocal()
    try:
        # Seed primary tables if they are empty
        if db.query(Career).count() == 0:
            df = pd.read_csv('careers_data.csv')
            for _, row in df.iterrows(): db.add(Career(name=row['name'], description=row['description']))
            db.commit()
            print("Careers seeded.")

        if db.query(Skill).count() == 0:
            df = pd.read_csv('skills_data.csv')
            for _, row in df.iterrows(): db.add(Skill(name=row['name']))
            db.commit()
            print("Skills seeded.")

        if db.query(College).count() == 0:
            df = pd.read_csv('colleges_data.csv')
            for _, row in df.iterrows(): db.add(College(name=row['name'], location=row['location']))
            db.commit()
            print("Colleges seeded.")

        if db.query(Course).count() == 0:
            df = pd.read_csv('courses_data.csv')
            for _, row in df.iterrows(): db.add(Course(name=row['name'], stream=row['stream'], duration_years=row['duration_years']))
            db.commit()
            print("Courses seeded.")

        print("Primary data tables are populated.")

        # Create relationships
        if db.query(career_skill_association).count() == 0:
            df_map = pd.read_csv('career_skills_map.csv')
            for _, row in df_map.iterrows():
                c = db.query(Career).filter_by(name=row['career_name']).first()
                s = db.query(Skill).filter_by(name=row['skill_name']).first()
                if c and s: c.skills.append(s)
            db.commit()
            print("Career-skill relationships created.")

        if db.query(college_course_association).count() == 0:
            df_map = pd.read_csv('college_courses_map.csv')
            for _, row in df_map.iterrows():
                c = db.query(College).filter_by(name=row['college_name']).first()
                o = db.query(Course).filter_by(name=row['course_name']).first()
                if c and o: c.courses.append(o)
            db.commit()
            print("College-course relationships created.")

        # --- ADD THIS NEW SECTION ---
        if db.query(career_course_association).count() == 0:
            print("Creating career-course relationships...")
            df_map = pd.read_csv('career_courses_map.csv')
            for _, row in df_map.iterrows():
                c = db.query(Career).filter_by(name=row['career_name']).first()
                o = db.query(Course).filter_by(name=row['course_name']).first()
                if c and o: c.courses.append(o)
            db.commit()
            print("Career-course relationships created.")
        else:
            print("Career-course relationships already exist.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_data()