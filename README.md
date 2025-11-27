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
