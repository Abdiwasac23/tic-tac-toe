# Tic Tac Toe (Flask + Tailwind)

A simple Tic Tac Toe demo using Flask for the backend and vanilla JS + Tailwind CSS for the frontend.

## Requirements
- Python 3.10+ (virtualenv recommended)

## Quick start (PowerShell)
```powershell
# create & activate a virtualenv (if you don't already have one)
python -m venv .venv
& .\.venv\Scripts\Activate.ps1

# install dependencies
pip install -r requirements.txt

# run the app
& .\.venv\Scripts\python.exe app.py

# open http://127.0.0.1:5000 in your browser
```

## Notes
- This app uses the Flask development server (debug mode). Do not use this configuration in production.
- Scores are stored in-memory and are shared across users for the running server process. For multi-user persistence, consider using sessions or a small database.

## Development
- To update dependencies: `pip install <package>` and then `pip freeze > requirements.txt`.
- To run tests (not included), add a `tests/` folder and use `pytest`.
