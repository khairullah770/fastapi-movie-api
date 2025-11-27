📝 Full Detailed Description (Use in GitHub README.md)
🎬 FastAPI Movie API

This project is a simple and beginner-friendly REST API built using FastAPI.
It allows users to manage movie data including:

Movie Name

Genre

Release Year

Budget

Revenue

Director Info

Duration

Rating

Language

Poster

The API supports multiple operations such as fetching all movies, filtering by genre or language, adding new movies, updating existing ones, and deleting movie records.

🚀 Features

FastAPI framework for high-performance APIs

Pydantic Models for data validation

JSON file used as a lightweight local database

Organized endpoints (GET, POST, PUT, DELETE)

Supports dynamic searching (by ID, genre, name)

Easy to extend and customize

📂 Project Structure
project1/
│── movie.py            # Main FastAPI file
│── movies.json         # Local JSON database
│── requirements.txt    # Required Python dependencies
│── README.md           # Documentation

▶️ How to Run the Project
1. Clone the Repository
git clone https://github.com/your-username/fastapi-movie-api.git
cd fastapi-movie-api

2. Create & Activate Virtual Environment
python -m venv env
env\Scripts\activate        # Windows

3. Install Requirements
pip install -r requirements.txt

4. Start FastAPI Server
uvicorn movie:app --reload

✔ Server will run at:

👉 http://127.0.0.1:8000

👉 Swagger Docs: http://127.0.0.1:8000/docs
