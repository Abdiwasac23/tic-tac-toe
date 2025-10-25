import sys

# Simple CLI Tic-Tac-Toe starter: phases 1-3
# Run with: python tictactoe.py

BOARD_TEMPLATE = [str(i+1) for i in range(9)]


def display_board(board):
    rows = [board[i:i+3] for i in range(0, 9, 3)]
    print('\n'.join([' {} | {} | {} '.format(*r) for r in rows]))
    print()


def check_winner(board):
    combos = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a,b,c in combos:
        if board[a] == board[b] == board[c] and board[a] in ('X','O'):
            return board[a]
    if all(cell in ('X','O') for cell in board):
        return 'draw'
    return None


def main():
    board = [' ']*9
    print('Welcome to Tic-Tac-Toe (CLI starter)')
    print('Rules: 3 in a row wins; board is 3x3; X goes first.')
    display_board(BOARD_TEMPLATE)

    while True:
        display_board([board[i] if board[i] != ' ' else str(i+1) for i in range(9)])
        choice = input('Enter position (1-9) to place X (or q to quit): ').strip()
        if choice.lower() in ('q','quit'):
            print('Goodbye')
            sys.exit(0)
        if not choice.isdigit():
            print('Please enter a number 1-9')
            continue
        pos = int(choice)-1
        if pos < 0 or pos > 8:
            print('Number must be 1-9')
            continue
        if board[pos] != ' ':
            print('That spot is already taken')
            continue
        board[pos] = 'X'
        winner = check_winner(board)
        if winner:
            display_board(board)
            if winner == 'draw':
                print("It's a draw")
            else:
                print(f'{winner} wins!')
            break
        # For phases 1-3 we stop here (no AI yet). You can extend this to add AI.

if __name__ == '__main__':
    main()
