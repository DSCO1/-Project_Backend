from fastapi import FastAPI
# CORRECTED: Using an absolute import starting from 'app'
from app.api.endpoints import recommendations, colleges, careers, skills, users

app = FastAPI()

app.include_router(recommendations.router, prefix="/api", tags=["Recommendations"])
app.include_router(colleges.router, prefix="/api", tags=["Colleges"])
app.include_router(careers.router, prefix="/api", tags=["Careers"])
app.include_router(skills.router, prefix="/api", tags=["Skills"])
app.include_router(users.router, prefix="/api", tags=["Users"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Career Advisor API"}