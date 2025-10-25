# Tic-Tac-Toe — Very Simple 5-Phase Guide

Short and human. Five clear phases. One sentence goal for each. Small deliverable for each phase.

Project idea
- You play X. Computer plays O. 3-in-a-row wins on a 3×3 board.

Quick run
```powershell
python tictactoe.py
```

If you want a virtual environment:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python tictactoe.py
```

The five phases (very simple)

1) Phase 1 — Setup and Rules
- Goal: get ready and know the rules.
- Do: create a file `tictactoe.py`. Write the rule sentence: "3 in a row wins; board is 3×3; X goes first.".
- Deliverable: `tictactoe.py` that prints a short welcome message.

2) Phase 2 — Make and show the board
- Goal: show the board so a person can pick a spot.
- Do: keep the board as a list of 9 items. Print it as three rows. Show empty spots as numbers 1–9.
- Deliverable: printed board like:
  1 | 2 | 3
  ---------
  4 | 5 | 6
  ---------
  7 | 8 | 9

3) Phase 3 — Let the player move
- Goal: let the player put X on the board safely.
- Do: ask for a number 1–9, check it is a number, check the spot is empty, then put 'X' there.
- Deliverable: player types a number and sees X appear.

4) Phase 4 — Win or draw check
- Goal: stop the game when someone wins or when there is a draw.
- Do: add `check_winner(board)` that returns 'X', 'O', or None. If no empty cells and no winner → draw.
- Deliverable: program prints "X wins", "O wins" or "It's a draw" and stops.

5) Phase 5 — Computer opponent and play loop
- Goal: make the computer play and make the game playable.
- Do: first add `computer_move_random(board)` which picks a random empty spot. Then add `computer_move_minimax(board)` for a perfect (hard) AI. Make a loop that alternates turns and prints the board after each move.
- Deliverable: a playable game. In hard mode the computer should not lose.

Short tips
- Map input 1–9 to indices 0–8.
- After each move, check for a winner immediately.
- Minimax should return both (score, best_move_index).

What to hand in
- `tictactoe.py` — the program
- `REPORT.md` or `README.md` — one short paragraph about Minimax and one example game
- Optional: `tests/test_game.py` with a few tests

Want me to add starter code?
- I can create a small `tictactoe.py` that covers phases 1–3 (board + player moves).
- Or I can add tests skeleton in `tests/test_game.py`.

Tell me which and I'll add it now.
# Tic-Tac-Toe Mini-Project Guide (Student Version)

This document is a tailored, step-by-step guide matching the Mini Project phases you provided. It describes exactly what to implement, which files to submit, how to run and test the program, and how the project can be graded.

## Overview
- Objective: Build a command-line Tic-Tac-Toe game where the student plays X and the computer plays O. The final program should include two AI modes: Easy (random) and Hard (Minimax).
- Deliverables: a Python script `tictactoe.py`, a short `REPORT.md` or `README.md` describing Minimax, and tests in `tests/test_game.py`.

## Required files (what to submit)
- `tictactoe.py` — main program (runnable with `python tictactoe.py`).
- `REPORT.md` or `README.md` — one page explaining your approach and Minimax with one sample game.
- `tests/test_game.py` — pytest tests for winner detection and at least one Minimax decision.
- `requirements.txt` — only if you use external libraries; otherwise leave it empty or omit.

## How to run (PowerShell commands)
From the project root (where `tictactoe.py` is):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python tictactoe.py
```

Or, without a virtual environment:

```powershell
python tictactoe.py
```

## Phase-by-phase tasks, acceptance criteria, and hints

Phase 0 — Setup and Introduction
- Tasks:
  - Create `tictactoe.py` and commit it to your repo.
  - Ensure Python is installed (`python --version`).
  - Note game rules in `README.md`.
- Acceptance: file exists and project run command prints a short welcome message.

Phase 1 — Board representation and display
- Tasks:
  - Represent the 3×3 board as a list of length 9.
  - Display empty spots as numbers 1–9 so users can choose them.
  - Show the board in three rows with separators.
- Acceptance: `display_board()` prints three rows and shows numbered empty cells.

Phase 2 — Let the player move
- Tasks:
  - Prompt the user to enter a number 1–9.
  - Validate input: numeric, in range, and cell empty.
  - Apply move as X.
- Acceptance: invalid input is rejected with an error message; valid input updates board.

Phase 3 — Win and draw detection
- Tasks:
  - Implement `check_winner(board)` returning `'X'`, `'O'`, or `None`.
  - Detect draw when the board is full and there's no winner.
- Acceptance: correct detection for all 8 winning lines and draw state.

Phase 4 — Computer moves (random then Minimax)
- Tasks:
  - Implement `computer_move_random(board)`.
  - Implement `computer_move_minimax(board)` using Minimax.
  - Minimax scoring: +1 for O (computer) win, -1 for X (player) win, 0 for tie.
- Acceptance: on `hard` difficulty, the computer never loses (best result is draw or computer win).

Implementation hints for Minimax:
- Base case: check for winner or draw.
- For each empty cell: simulate move, recurse with swapped player, collect scores.
- The computer chooses the move with the maximum score; the player is assumed to minimize.
- Return both (score, move_index) from the recursive function.

Phase 5 — Interactive gameplay
- Tasks:
  - Build a game loop that alternates turns (X first), prints the board after each move, and ends on win/draw.
  - Allow user to choose difficulty at start: `easy` or `hard`.
- Acceptance: playable game where the player can type moves until game ends.

Phase 6 — Optional UX enhancements
- Add messages such as "Computer is thinking..." and "Play again?".
- Add a two-player local mode.
- (Optional) Add a GUI with `tkinter` or a web UI with Flask.

Phase 7 — Tests, report, and presentation
- Tasks:
  - Add unit tests for `check_winner` and for a deterministic Minimax scenario.
  - Write `REPORT.md` explaining Minimax and include one example game demonstrating that Minimax prevents a loss.
- Acceptance: tests run and pass with `pytest`.

## Suggested function contracts
- display_board(board) -> None
- check_winner(board) -> 'X' | 'O' | None
- player_move(board, position:int) -> bool
- computer_move_random(board) -> int
- computer_move_minimax(board) -> int
- minimax(board, is_maximizing:bool) -> (score:int, best_index:int)

## Minimal pytest tests to include
- `test_empty_board_no_winner`
- `test_detect_row_column_diagonal_wins`
- `test_detect_draw`
- `test_minimax_blocks_or_wins`

Example test snippet (informational):

```python
from tictactoe import check_winner, computer_move_minimax

def test_row_win():
    board = ['X','X','X',' ',' ',' ',' ',' ',' ']
    assert check_winner(board) == 'X'

def test_minimax_blocks_loss():
    board = ['X','X',' ','O',' ',' ',' ',' ',' ']
    move = computer_move_minimax(board)
    assert move == 2
```

## Grading rubric (suggested weights)
- 30% Implementation of board and input validation
- 25% Win/draw detection correctness
- 25% Minimax correctness (hard difficulty)
- 10% UX and messages
- 10% Tests and documentation

## Example run (user flow)
1. Program: "Choose difficulty (easy/hard): " → user types `hard`.
2. Program prints board with numbered empty spots.
3. Prompt: "Enter position (1-9): " → user types `5`.
4. Program prints updated board, checks for end condition, then computer moves.
5. Repeat until final message: "X wins!" / "O wins!" / "It's a draw.".

## Hints, pitfalls, and tips
- Map user input 1–9 to indices 0–8.
- Always check for a winner before running Minimax recursion on a state.
- Return both score and index from Minimax so you can pick the actual move.

## Stretch goals (extra credit)
- Two-player local mode.
- Persistent high scores (JSON file).
- Alpha-beta pruning and timing comparison.

## Submission checklist
- [ ] `tictactoe.py`
- [ ] `tests/test_game.py`
- [ ] `REPORT.md` or `README.md` explaining Minimax
- [ ] Optional `requirements.txt` (if used)

---

Tell me what you'd like me to do next:
- Generate a starter `tictactoe.py` implementing Phases 0–3
- Create the `tests/test_game.py` skeleton
- Convert this document into `README.md` and commit it now

I'll do the selected next step if you pick one.
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