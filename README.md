# Career Advisor Backend API 🚀

This is the backend service for the "One-Stop Personalized Career & Education Advisor" project, built for the Smart India Hackathon (SIH). It provides a RESTful API to deliver personalized career and education recommendations to students.

---
## ✨ Features

* **Personalized Recommendations:** Core engine that suggests careers based on a user's quiz answers and academic profile.
* **Relational Data Model:** Utilizes a complete relational database to link careers, skills, colleges, and courses.
* **User Profile Management:** Endpoints to create, update, and retrieve user profiles (linked via Firebase Auth UID).
* **RESTful API:** A full suite of API endpoints for all frontend functionalities.
* **Automated API Documentation:** Interactive API documentation powered by FastAPI & Swagger UI.

---
## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **Framework:** FastAPI
* **Database:** PostgreSQL (managed with Docker)
* **ORM:** SQLAlchemy
* **Data Validation:** Pydantic
* **Containerization:** Docker & Docker Compose
* **Application Server:** Uvicorn

---
## 📂 Project Structure

The project follows a modular architecture to separate concerns:

```
app/
|-- api/
|   |-- endpoints/
|       |-- careers.py
|       |-- colleges.py
|       |-- recommendations.py
|       |-- skills.py
|       |-- users.py
|-- core/
|-- models/
|-- schemas.py
|-- services/
|-- main.py
scripts/
```

## ⚙️ Setup and Installation

To run this project locally, follow these steps:

1.  **Clone the Repository:**
    ```bash
    git clone <your-repo-url>
    cd career-advisor-backend
    ```

2.  **Create a Virtual Environment:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Start the Database:**
    *Ensure Docker Desktop is running.*
    ```bash
    docker-compose up -d
    ```

5.  **Seed the Database (First Time Only):**
    *Run this script to populate the database with initial data.*
    ```bash
    python -m scripts.seed_database
    ```

6.  **Run the Backend Server:**
    ```bash
    uvicorn app.main:app --reload
    ```
    The server will be running at `http://127.0.0.1:8000`.

---
## Endpoints

The interactive API documentation is the best place to see and test all endpoints. It is available at `http://127.0.0.1:8000/docs`.

| Method | Endpoint                               | Description                                      |
| :----- | :------------------------------------- | :----------------------------------------------- |
| `POST` | `/api/users/`                          | Create or update a user's profile.               |
| `GET`  | `/api/users/{user_id}`                 | Retrieve a user's profile by their ID.           |
| `POST` | `/api/users/{user_id}/recommendations/`| Get personalized career recommendations.         |
| `GET`  | `/api/careers/`                        | Get a list of all careers and their skills.      |
| `GET`  | `/api/colleges/`                       | Get a list of all colleges and their courses.    |
| `GET`  | `/api/skills/`                         | Get a list of all skills and their careers.      |

This README gives a complete and professional overview of the entire backend you've built.
