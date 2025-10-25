# Tic-Tac-Toe Mini-Project — Short Report

Purpose
- Build a simple Tic-Tac-Toe game where the student plays X and the computer plays O. The project demonstrates basic programming concepts (data structures, input validation, control flow) and a simple AI technique (Minimax).

What I built (summary)
- A command-line Tic-Tac-Toe program (`tictactoe.py`) that prints a 3×3 board, accepts player moves (1–9), checks for wins/draws, and supports two AI modes:
  - Easy: random valid move
  - Hard: Minimax (optimal play)

Five short phases (what the student completes)
1. Setup & rules — create `tictactoe.py` and note the rules: 3 in a row wins; board is 3×3; X goes first.
2. Board display — represent the board as a list of 9 items and print it as three rows; empty spots show as numbers 1–9.
3. Player moves — ask for input 1–9, validate it, and place X on the board.
4. Win/draw detection — implement `check_winner(board)` and stop the game when someone wins or the board is full.
5. Computer and loop — implement `computer_move_random(board)` and `computer_move_minimax(board)`; build the main loop to alternate turns and finish the game.

How to run
1. From the project folder run:

```powershell
python tictactoe.py
```

2. (Optional) Create a virtual environment and install dependencies if provided in `requirements.txt`.

Minimax — short explanation
- Minimax is a recursive search that assumes the opponent plays optimally. The algorithm explores all possible moves to terminal states and assigns scores: +1 (computer win), -1 (player win), 0 (tie). The computer chooses the move that maximizes its score while assuming the player chooses moves that minimize the computer's score.

Deliverables
- `tictactoe.py` — program source
- `REPORT.md` — this short report
- Optional: `tests/test_game.py` — pytest tests for winner detection and Minimax behavior

Grading suggestions (instructor)
- Board & input validation: 30%
- Win/draw detection: 25%
- Minimax correctness: 25%
- Usability & messages: 10%
- Tests & documentation: 10%

Sample quick check (manual)
- Empty board → run program, no winner.
- Place X in 1,2,3 → `check_winner` should report X wins.
- On hard difficulty, computer should never lose.

If you want, I can now:
- Add a starter `tictactoe.py` (phases 1–3), or
- Add `tests/test_game.py` skeleton, or
- Export this report as a PDF and add it to the repo.
