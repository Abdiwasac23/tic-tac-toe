# Tic Tac Toe (Flask + Tailwind)

A small Tic Tac Toe web game using Python + Flask for the backend and vanilla JavaScript + Tailwind CSS for the frontend.

## Requirements
- Python 3.10 or newer installed
- (Optional) Git if you plan to clone the repo

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
- This uses the Flask development server (debug). For production use a WSGI server (Waitress/gunicorn) and HTTPS.
- Scores are stored in memory and will reset when the server restarts. Use sessions or a DB for persistence.

## Development
- To update dependencies: `pip install <package>` and then `pip freeze > requirements.txt`.
- To run tests (optional, recommended before pushing changes), add a `tests/` folder and use `pytest`.

This README provides step-by-step instructions to set up and run the game on a new device.

Contents
- `app.py` — Flask backend
- `templates/index.html` — frontend UI and client JS
- `static/` — CSS and Tailwind config
- `tests/` — unit tests (pytest)
- `requirements.txt`, `start.ps1` (Windows helper)

Quick summary: You can run the game locally and open http://127.0.0.1:5000 in your browser. Use the Mode selector to pick Single-player (vs AI) or Two-player (local).

1) Copy the project to the new device
- From GitHub (example):
```bash
git clone https://github.com/<yourname>/tic_tac_toe.git
cd tic_tac_toe
```
- Or copy the folder by USB, network share, or zip/unzip.

2) Windows (PowerShell) — one-command start (recommended)
- Open PowerShell in the project folder and run the helper script:
```powershell
# if running for the first time you may need to allow script execution in this session
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
.\start.ps1
```
- The script will:
	- Create `.venv` if missing
	- Activate the virtual environment
	- Install packages from `requirements.txt`
	- Prompt to run tests (optional)
	- Start the Flask app bound to all interfaces (0.0.0.0:5000)

3) Windows (manual steps)
- Open PowerShell and run:
```powershell
cd "C:\path\to\tic_tac_toe"
python -m venv .venv
& .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
& .\.venv\Scripts\python.exe app.py
```
- Open http://127.0.0.1:5000 in your browser.

4) macOS / Linux (bash)
```bash
cd /path/to/tic_tac_toe
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```
Open http://127.0.0.1:5000 in your browser.

5) Run tests (optional, recommended before pushing changes)
```powershell
# Windows PowerShell
& .\.venv\Scripts\python.exe -m pytest -q
```
```bash
# macOS / Linux
python -m pytest -q
```

6) Make the app accessible from other devices on the same LAN
- Run the Flask server on all interfaces so other devices can connect to your machine's LAN IP:
```powershell
# using flask (PowerShell)
$env:FLASK_APP='app.py'
& .\.venv\Scripts\python.exe -m flask run --host=0.0.0.0 --port=5000
```
Or edit `app.py` to call `app.run(host='0.0.0.0', port=5000)` and run `python app.py`.
- Find your machine's LAN IP (Windows):
```powershell
ipconfig
```
Open from another device at http://<LAN-IP>:5000

7) Share the app publicly (quick method): ngrok (recommended for demos)
- Install ngrok (https://ngrok.com/), then run (after server is running):
```powershell
ngrok http 5000
```
- ngrok prints a public HTTPS URL you can share. Close the tunnel when done.

8) Troubleshooting
- `Permission denied` when running `start.ps1`: run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` first.
- `Connection refused` from another device: ensure server is listening on 0.0.0.0 and firewall allows port 5000.
- To open Windows firewall for the port (Admin PowerShell):
```powershell
New-NetFirewallRule -DisplayName "TicTacToe 5000" -Direction Inbound -LocalPort 5000 -Protocol TCP -Action Allow
```

9) Notes & tips
- Modes: Single-player (player X vs AI O) and Two-player (two people sharing the UI) are available via the Mode selector.
- AI levels: easy (random), medium (heuristic), hard (Minimax/unbeatable).

If you want I can add a `start.sh` for macOS/Linux or create a one-click zip of the project for easy copying to another device.
