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
