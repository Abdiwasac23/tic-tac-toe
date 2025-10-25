
from flask import Flask, render_template, jsonify, request, session
import random
import uuid


app = Flask(__name__)
app.secret_key = 'replace-this-with-a-random-secret-key'  # Needed for session

# In-memory store for per-session game state (demo only, not for production)
games = {}

scores = {"player": 0, "ai": 0, "draw": 0}

def check_winner(board):
    combos = [(0,1,2),(3,4,5),(6,7,8),
              (0,3,6),(1,4,7),(2,5,8),
              (0,4,8),(2,4,6)]
    for a,b,c in combos:
        if board[a] == board[b] == board[c] and board[a] != "":
            return board[a]
    if "" not in board:
        return "draw"
    return None

def ai_move(board, level):
    empty = [i for i in range(9) if board[i] == ""]
    if not empty: return None

    if level == "easy":
        return random.choice(empty)
    
    if level == "medium":
        for i in empty:
            copy = board[:]
            copy[i] = "O"
            if check_winner(copy) == "O":
                return i
        for i in empty:
            copy = board[:]
            copy[i] = "X"
            if check_winner(copy) == "X":
                return i
        return random.choice(empty)
    
    if level == "hard":
        # Use Minimax to pick an optimal move for the AI (O)
        def minimax(board_state, is_maximizing):
            winner = check_winner(board_state)
            if winner == 'O':
                return 1
            if winner == 'X':
                return -1
            if winner == 'draw':
                return 0

            moves = [i for i in range(9) if board_state[i] == ""]
            if is_maximizing:
                best_score = -999
                for m in moves:
                    board_state[m] = 'O'
                    score = minimax(board_state, False)
                    board_state[m] = ''
                    if score > best_score:
                        best_score = score
                return best_score
            else:
                best_score = 999
                for m in moves:
                    board_state[m] = 'X'
                    score = minimax(board_state, True)
                    board_state[m] = ''
                    if score < best_score:
                        best_score = score
                return best_score

        best_moves = []
        best_score = -999
        for m in empty:
            board[m] = 'O'
            score = minimax(board, False)
            board[m] = ''
            if score > best_score:
                best_score = score
                best_moves = [m]
            elif score == best_score:
                best_moves.append(m)

        # prefer center if it's among best moves, then corners, otherwise pick randomly
        center = 4
        corners = [0, 2, 6, 8]
        if center in best_moves:
            return center
        corner_moves = [c for c in corners if c in best_moves]
        if corner_moves:
            return random.choice(corner_moves)
        return random.choice(best_moves)


@app.route('/')
def index():
    # On first visit, create a new game session
    if 'game_id' not in session:
        session['game_id'] = str(uuid.uuid4())
    return render_template('index.html')


@app.route('/start', methods=['POST'])
def start():
    """Start a new game: set mode and level, reset board and scores."""
    data = request.get_json() or {}
    mode = data.get('mode', 'single')
    level = data.get('level', 'easy')
    game_id = session.get('game_id')
    if not game_id:
        game_id = str(uuid.uuid4())
        session['game_id'] = game_id
    # Reset game state
    games[game_id] = {
        'board': [""] * 9,
        'turn': 'X',
        'mode': mode,
        'level': level,
        'scores': {"player": 0, "ai": 0, "draw": 0},
        'winner': None
    }
    return jsonify({"ok": True, "board": [""] * 9, "turn": 'X', "mode": mode, "level": level, "scores": {"player": 0, "ai": 0, "draw": 0}})


@app.route('/move', methods=['POST'])
def move():
    data = request.get_json() or {}
    index = data.get('index')
    game_id = session.get('game_id')
    if not game_id or game_id not in games:
        return jsonify({"error": "no active game"}), 400
    game = games[game_id]
    board = game['board']
    turn = game['turn']
    mode = game['mode']
    level = game['level']
    scores = game['scores']
    winner = game['winner']

    # Validate index
    if not isinstance(index, int) or not (0 <= index < 9):
        return jsonify({"error": "invalid index"}), 400
    if board[index] != "":
        return jsonify({"error": "cell not empty"}), 400
    if winner:
        return jsonify({"error": "game over"}), 400

    # Apply player's move
    board[index] = turn

    # Check for winner after player's move
    winner = check_winner(board)
    if winner:
        game['winner'] = winner
        if winner == "X":
            scores["player"] += 1
        elif winner == "O":
            scores["ai"] += 1
        else:
            scores["draw"] += 1
        return jsonify({"board": board, "winner": winner, "scores": scores, "turn": turn})

    # If single-player and it's X's turn, AI plays as O
    if mode == 'single' and turn == 'X':
        ai_idx = ai_move(board, level)
        if ai_idx is not None and board[ai_idx] == "":
            board[ai_idx] = 'O'
            # Check for winner after AI move
            winner = check_winner(board)
            if winner:
                game['winner'] = winner
                if winner == "X":
                    scores["player"] += 1
                elif winner == "O":
                    scores["ai"] += 1
                else:
                    scores["draw"] += 1
                game['turn'] = 'X'  # X always starts next game
                return jsonify({"board": board, "winner": winner, "scores": scores, "turn": 'X'})
        # If no winner, next turn is X
        game['turn'] = 'X'
        return jsonify({"board": board, "winner": None, "scores": scores, "turn": 'X'})

    # Two-player: alternate turns
    game['turn'] = 'O' if turn == 'X' else 'X'
    return jsonify({"board": board, "winner": None, "scores": scores, "turn": game['turn']})

if __name__ == '__main__':
    app.run(debug=True)
