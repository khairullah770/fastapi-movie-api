<<<<<<< HEAD
# Movie API

This FastAPI app serves movie data from `Movies_Json.txt`. By default, the app will load that file from the same directory.

## Setup

1. Install dependencies:

```powershell
pip install -r requirements.txt
```

2. Run the app with Uvicorn:

```powershell
python -m uvicorn movie:app --reload --host 127.0.0.1 --port 8000
```

3. Endpoints
- `GET /movies` — list all movies
- `GET /movies/{id}` — get a specific movie
- `GET /movies/genre/{genre}` — filter by genre
- ... (other endpoints are available, see source)
- `POST /movies/reload` — reload the data from `Movies_Json.txt` without restarting the server

## Notes
- `Movies_Json.txt` contains the MOVIES array and some model code; the loader extracts only the top-level array and ignores other content in the file.
- You can set the `MOVIES_FILE` environment variable to point to a different file.

## Add to GitHub

To add this project to GitHub from your local machine, follow these steps.

1. Initialize git (if you haven't already):

```powershell
git init
git branch -M main
git add .
git commit -m "Initial commit: Movie API using Movies_Json.txt"
```

2. Create a GitHub repo and push

If you have the GitHub CLI installed and are logged in, run:

```powershell
gh repo create <your-username>/<repo-name> --public --source . --remote origin --push
```

Or create the repository on GitHub via the web UI and then:

```powershell
git remote add origin https://github.com/<your-username>/<repo-name>.git
git push -u origin main
```

3. When added to GitHub, CI via GitHub Actions will run tests automatically.

4. Optional: add a `README.md` badge listing the build status, and add more details to your project description to showcase it in your portfolio.

If you'd like, I can run the above `git`/`gh` commands here to create the repo and push - let me know if you want that and confirm the repo name.
=======
**🎬 FastAPI Movie API — A Modern REST Backend for Movie Data**

Welcome to the FastAPI Movie API, a high-performance, clean, and beginner-friendly REST API designed for movie data management.
Built with FastAPI, powered by Pydantic validation, and using a simple JSON file as storage, this project is perfect for students, beginners, and developers learning how to build APIs.

This API demonstrates how to structure a Python backend, create endpoints, handle validation, and work with dynamic search functionalities — all in a fast and elegant way.

**✨ Features**

✔ Super-fast performance powered by FastAPI
✔ Clean and structured endpoints (GET, POST, PUT, DELETE)
✔ Fully typed Pydantic Models
✔ JSON-based lightweight local database
✔ Filter movies by Genre, Language, ID, etc.
✔ Easy to extend and customize
✔ Swagger UI automatically available
✔ Beginner-friendly project structure

**📁 Project Structure**
project1/
│── movie.py              # Main FastAPI application
│── movies.json           # Local database
│── requirements.txt      # Python dependencies
│── README.md             # Documentation


**🚀 How to Run This Project**
1️⃣ Clone the Repository
git clone https://github.com/your-username/fastapi-movie-api.git
cd fastapi-movie-api

2️⃣ Create & Activate Virtual Environment
python -m venv env
env\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Start the FastAPI Server
uvicorn movie:app --reload

Your API is now live at:

🌐 http://127.0.0.1:8000

📘 Swagger Docs: http://127.0.0.1:8000/docs

📗 ReDoc Docs: http://127.0.0.1:8000/redoc

<img width="716" height="387" alt="image" src="https://github.com/user-attachments/assets/98e8f691-9482-4b63-94f0-65b2f44969f6" />

🔧 Tech Stack

FastAPI — Modern high-performance Python web framework

Pydantic — Data validation and settings management

Uvicorn — Lightning-fast ASGI server

JSON Storage — Simple file-based data handling

**🎯 Purpose of This Project**

This project is ideal for:

Students learning backend development

Developers practicing API design

Beginners exploring FastAPI

Anyone building a simple movie database app

Portfolio / GitHub projects

**❤️ Contributions**

Feel free to fork, improve, and submit pull requests.
Feedback and suggestions are always welcome!
>>>>>>> eb58b57005e652f60b63c5c108891dd8bc244ff2
