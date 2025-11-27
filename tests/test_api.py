from fastapi.testclient import TestClient
from movie import app

client = TestClient(app)


def test_get_movies():
    response = client.get("/movies")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    # If the data is loaded from Movies_Json.txt, it should contain at least one movie
    assert len(data) >= 1


def test_get_movie_id_1():
    response = client.get("/movies/1")
    assert response.status_code == 200
    movie = response.json()
    assert movie["ID"] == 1