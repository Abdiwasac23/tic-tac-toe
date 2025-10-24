## Running on another device

After downloading or copying the project to a new computer:

1. Make sure Python 3.10+ is installed on the new device.
2. Open PowerShell (Windows) or Terminal (macOS/Linux) in the project folder.
3. Run these commands:
	```powershell
	python -m venv .venv
	& .\.venv\Scripts\Activate.ps1
	pip install -r requirements.txt
	& .\.venv\Scripts\python.exe app.py
	```
	(On macOS/Linux, use `source .venv/bin/activate` and `python app.py` instead.)
4. Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

The game will be ready to play!


# Tic Tac Toe

This is a simple web-based Tic Tac Toe game built with Python (Flask) for the backend and JavaScript (with Tailwind CSS) for the frontend.

## Features
- 3x3 grid, classic Tic Tac Toe rules
- Single-player (vs AI) and two-player (local) modes
- Three AI difficulty levels: easy, medium, hard
- Score tracking for player, AI, and draws
- Automatic new round after win or draw
- Responsive UI

## Requirements
- Python 3.10 or newer
- (Optional) Git to clone the repo

## Setup & Run
1. Open PowerShell in the project folder.
2. Run these commands:
	```powershell
	python -m venv .venv
	& .\.venv\Scripts\Activate.ps1
	pip install -r requirements.txt
	& .\.venv\Scripts\python.exe app.py
	```
3. Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## How to play
- Select mode: Single-player (play against AI) or Two-player (play with a friend on the same device)
- Select AI difficulty (easy, medium, hard) for single-player
- Click a cell to make your move
- The game will show the winner or draw and automatically start a new round
- Scores are shown below the board

## Notes
- This uses the Flask development server (for local use and learning)
- Scores reset when the server restarts
- For production, use a proper server and database

Enjoy!

## Deploying (quick)
If you want to deploy the app to a simple host (Render, Railway, Heroku):

1. Ensure `requirements.txt` includes `gunicorn` (already added).
2. Add a start command in the host settings or use the `Procfile` provided:

```
web: gunicorn app:app --bind 0.0.0.0:$PORT
```

3. Connect your GitHub repo in the host UI and create a new Web Service — the host will build and run the app and give you a public URL.

Note: this project uses the Flask development server locally; gunicorn is used for production-like hosting.


