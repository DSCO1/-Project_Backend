from fastapi import FastAPI
from .api.endpoints import recommendations

app = FastAPI()

# Include the router from our recommendations file
app.include_router(recommendations.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Career Advisor API"}