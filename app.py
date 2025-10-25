from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

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
    return render_template('index.html')

@app.route('/move', methods=['POST'])
def move():
    data = request.get_json() or {}
    board = data.get('board')
    ai_level = data.get('level')
    mode = data.get('mode', 'single')
    index = data.get('index')
    player = data.get('player', 'X')

    # Basic validation: ensure board is a list of length 9
    if not isinstance(board, list) or len(board) != 9:
        return jsonify({"error": "invalid board"}), 400

    # ensure board items are valid
    if any(cell not in ('', 'X', 'O') for cell in board):
        return jsonify({"error": "invalid board contents"}), 400

    # validate index
    if not isinstance(index, int) or not (0 <= index < 9):
        return jsonify({"error": "invalid index"}), 400

    # Mode-specific validation
    if mode == 'single':
        if ai_level not in ("easy", "medium", "hard"):
            return jsonify({"error": "invalid level"}), 400
        # ensure the player's chosen cell is X and is empty before (client should set X)
        if board[index] != 'X':
            return jsonify({"error": "index must contain player's move (X)"}), 400
        # simple consistency check: X count should be >= O count and difference reasonable
        x_count = board.count('X')
        o_count = board.count('O')
        if x_count - o_count not in (0, 1):
            return jsonify({"error": "invalid move counts"}), 400

        # If player's move already produced a winner, don't let the AI play
        winner = check_winner(board)
        if not winner:
            move_index = ai_move(board, ai_level)
            if move_index is not None and board[move_index] == "":
                board[move_index] = "O"

    else:
        # two-player mode: validate player and that the board contains their move at index
        if player not in ('X', 'O'):
            return jsonify({"error": "invalid player"}), 400
        if board[index] != player:
            return jsonify({"error": "index must contain player's move"}), 400

    # Re-check winner after possible AI move
    winner = check_winner(board)
    if winner:
        if winner == "X":
            scores["player"] += 1
        elif winner == "O":
            scores["ai"] += 1
        else:
            scores["draw"] += 1

    return jsonify({"board": board, "winner": winner, "scores": scores})

if __name__ == '__main__':
    app.run(debug=True)
