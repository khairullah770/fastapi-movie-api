from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import json
import os

app = FastAPI()

# Default path to the movies text file. You can override with the MOVIES_FILE env var
MOVIES_FILE = os.getenv("MOVIES_FILE", "Movies_Json.txt")

# MOVIES will be loaded from the external file at startup
MOVIES: List[dict] = []


class Movie(BaseModel):
    ID: int
    MOVIENAME: str
    GENRE: str
    YEAROFRELEASE: int
    BUDGET: float
    REVENUE: float
    DIRECTORNAME: str
    DURATION: int
    RATING: str
    PRIMARYLANGUAGE: str
    POSTER: str


def _extract_json_list_from_text(text: str) -> str:
    """Find and return the JSON list substring (from the first '[' to its matching ']') in a file containing Python-style assignment or extra code.
    This expects a top-level list of objects like [ { ... }, { ... } ] and returns the JSON array string.
    Raises ValueError if not found or parentheses mismatch.
    """
    start = text.find("[")
    if start == -1:
        raise ValueError("No '[' found in file content")
    depth = 0
    for idx in range(start, len(text)):
        ch = text[idx]
        if ch == '[':
            depth += 1
        elif ch == ']':
            depth -= 1
            if depth == 0:
                return text[start: idx + 1]
    raise ValueError("No matching closing ']' found for the JSON array")


def load_movies_from_file(path: str) -> List[dict]:
    """Load the MOVIES array from the specified file. The file can contain extra text before/after the array (like a 'MOVIES=' assignment or class definitions)."""
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    # Extract the top-level JSON array substring and parse
    json_list_text = _extract_json_list_from_text(content)
    try:
        movies = json.loads(json_list_text)
    except json.JSONDecodeError as e:
        # JSON may sometimes be valid Python but not JSON; give a helpful error
        raise ValueError(f"Failed to decode JSON in {path}: {e}") from e
    if not isinstance(movies, list):
        raise ValueError("Movies data is not a JSON list")
    return movies


@app.on_event("startup")
def load_movies_on_startup():
    global MOVIES
    try:
        MOVIES = load_movies_from_file(MOVIES_FILE)
    except Exception as e:
        # If for any reason the file could not be loaded, we raise to catch early.
        raise RuntimeError(f"Could not load movies from {MOVIES_FILE}: {e}")

# Endpoint to get all movies
@app.get("/movies")
def get_movies():
    return MOVIES

#return movie by ID
@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    for movies in MOVIES:
        if movies["ID"] == movie_id:
            return movies
    raise HTTPException(status_code=404, detail="Movie not found")

# Endpoint to get movies by genre
@app.get("/movies/genre/{genre}")
def get_movies_by_genre(genre: str):
    genre_movies = [movie for movie in MOVIES if movie["GENRE"].lower() == genre.lower()]
    return genre_movies

# Endpoint to get movies by director
@app.get("/movies/director/{director_name}")
def get_movies_by_director(director_name: str):
    director_movies = [movie for movie in MOVIES if movie["DIRECTORNAME"].lower() == director_name.lower()]
    return director_movies 

# Endpoint to get movies by year of release
@app.get("/movies/year/{year}")
def get_movies_by_year(year: int):
    year_movies = [movie for movie in MOVIES if movie["YEAROFRELEASE"] == year]
    return year_movies 

# Endpoint to get movies by rating
@app.get("/movies/rating/{rating}")
def get_movies_by_rating(rating: str):
    rating_movies = [movie for movie in MOVIES if movie["RATING"].lower() == rating.lower()]
    return rating_movies     

# Endpoint to get movies by primary language
@app.get("/movies/language/{language}")
def get_movies_by_language(language: str):
    language_movies = [movie for movie in MOVIES if movie["PRIMARYLANGUAGE"].lower() == language.lower()]
    return language_movies

# Endpoint to get movies by budget range
@app.get("/movies/budget/{min_budget}/{max_budget}")
def get_movies_by_budget(min_budget: float, max_budget: float):
    budget_movies = [movie for movie in MOVIES if min_budget <= movie["BUDGET"] <= max_budget]
    return budget_movies   

# Endpoint to get movies by rating range
@app.get("/movies/revenue/{min_revenue}/{max_revenue}")
def get_movies_by_revenue(min_revenue: float, max_revenue: float):  
    revenue_movies = [movie for movie in MOVIES if min_revenue <= movie["REVENUE"] <= max_revenue]
    return revenue_movies

# Endpoint to get movies by duration range
@app.get("/movies/duration/{min_duration}/{max_duration}") 
def get_movies_by_duration(min_duration: int, max_duration: int):
    duration_movies = [movie for movie in MOVIES if min_duration <= movie["DURATION"] <= max_duration]
    return duration_movies

# Endpoint to get movies by name search
@app.get("/movies/name/{name}")
def get_movies_by_name(name: str):
    name_movies = [movie for movie in MOVIES if name.lower() in movie["MOVIENAME"].lower()]
    return name_movies


#Endpoint to create a new movie
@app.post("/movies")
def create_movie(movie: Movie):
    # Check if a movie with the same ID already exists
    for existing_movie in MOVIES:
        if existing_movie["ID"] == movie.ID:
            raise HTTPException(status_code=400, detail="Movie with this ID already exists")
    # Add the new movie to the MOVIES list
    MOVIES.append(movie.dict())
    return movie 

# Endpoint to update an existing movie by ID
@app.put("/movies/{movie_id}") 
def update_movie(movie_id: int, updated_movie: Movie):
    for index, existing_movie in enumerate(MOVIES):
        if existing_movie["ID"] == movie_id:
            MOVIES[index] = updated_movie.dict()
            return updated_movie
    raise HTTPException(status_code=404, detail="Movie not found")

# Endpoint to delete a movie by ID
@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: int):
    for index, existing_movie in enumerate(MOVIES):
        if existing_movie["ID"] == movie_id:
            del MOVIES[index]
            return {"message": "Movie deleted successfully"}
    raise HTTPException(status_code=404, detail="Movie not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)  
     
# movie.py --- IGNORE ---
# This file contains the FastAPI application for managing a movie database.
# It defines endpoints to create, read, update, and delete movie records,
# as well as to filter movies based on various criteria such as genre, director,
# year of release, rating, language, budget, revenue, duration, and name search.
# The movie data is loaded from an external text file (Movies_Json.txt) at startup.
# The Movie model is defined using Pydantic for data validation.
