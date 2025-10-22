# Tic Tac Toe — Assignment Documentation

This document describes the original problem, what I inspected, the issues found, how I fixed them, tests performed, how to run the game, and suggested next steps.

## Problem statement
You were given a simple Tic Tac Toe web app built with Flask (backend) and vanilla JavaScript + Tailwind (frontend). The instructor asked for a review and improvements with a short report explaining the problems found and how they were solved.

## What I inspected
- `app.py` — Flask backend providing `/` and `/move` endpoints and game logic (winner detection and AI move logic).
- `templates/index.html` — Frontend UI, game board rendering and client-side JS to send moves to the server.
- `static/style.css` — Small CSS for animation and transitions.

## Issues found (summary)
1. Backend accepted client-sent board without validation and allowed the AI to play even if the player's move had already produced a winner. This could lead to invalid state updates and incorrect scoring.
2. Frontend used `document.write` to generate the board, which is fragile and not recommended.
3. Frontend allowed rapid double-clicks or multiple inputs while waiting for the AI response, creating race conditions.
4. CSS/JS left classes in place without cleaning, which could cause visual inconsistencies.
5. Scores were stored in a module-level dictionary (`scores`) — fine for a demo but not per-user or persistent.
6. `hard` AI used heuristics but was not unbeatable (no Minimax).

## Changes made
1. Backend
   - Added input validation for `/move` ensuring `board` is a list of length 9 and `level` is valid.
   - Moved winner check to before AI move to avoid the AI placing a move after the player has already won.
   - Implemented a Minimax algorithm for the `hard` AI to make it unbeatable; added a tie-breaking preference for center then corners.

2. Frontend
   - Replaced `document.write` with DOM creation for the board cells.
   - Added an `awaiting` flag and visual disabling while waiting for the server so the user cannot double-click and send multiple moves.
   - Ensured color classes (`text-teal-300`, `text-rose-400`) are cleaned before applying the current state.

3. Project
   - Added tests (`tests/test_game.py`) covering `check_winner` and `ai_move` behaviors.
   - Added `pytest` to the dev environment and verified tests pass (6 passed).
   - Added `requirements.txt` and a minimal `README.md` with run instructions.
   - Added a `start.ps1` script to simplify starting the app on Windows (creates/activates venv, installs requirements, runs tests optionally, starts server bound to 0.0.0.0).
   - Added a GitHub Actions workflow `.github/workflows/python-app.yml` to run tests on push.

## Tests performed
- Unit tests: created `tests/test_game.py` with tests for win detection (rows, columns, diagonals, draw) and AI behavior (medium should block, hard prefers center on empty board). All tests passed locally.
- Manual run: started the Flask dev server and exercised the frontend to verify gameplay for easy/medium/hard.

## How to run (short)
1. Clone or copy the repo.
2. On Windows PowerShell:
```powershell
cd path\to\tic_tac_toe
.\start.ps1
```
This script will create and activate `.venv` if needed, install dependencies, run tests if you choose, and start the app.

Or manually:
```powershell
python -m venv .venv
& .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
& .\.venv\Scripts\python.exe app.py
```
Open http://127.0.0.1:5000 in your browser.

## Notes and recommendations
- The server uses Flask's development server; do not expose it to the internet for production use. For production use a WSGI server (Waitress/gunicorn) and HTTPS.
- Scores are stored in-memory; if per-user persistence is needed, use Flask sessions or a small database (SQLite).
- The Minimax implementation is recursive but fine for 3x3 Tic Tac Toe; no performance issues expected. For larger games consider alpha-beta pruning.
- Frontend accessibility improvements: keyboard support, ARIA roles, focus styles.

## Files changed/added
- Modified: `app.py`, `templates/index.html`, `static/style.css` (minor tweaks)
- Added: `tests/test_game.py`, `requirements.txt`, `README.md`, `DOCUMENTATION.md`, `start.ps1`, `.github/workflows/python-app.yml`

## Next steps (optional)
- Make server authoritative: send only player's move index to `/move` so server validates and applies moves (prevents tampering).
- Add per-user sessions and persistent scoring.
- Replace Flask dev server with a production WSGI server if exposing externally.
- Add more unit tests and integration tests (frontend automation).

---

If you'd like, I can tailor this document to the format your instructor wants (short report, bullet list, or a PDF). Tell me the preferred format and I will generate it.