import pytest
from app import check_winner, ai_move


def test_check_winner_rows():
    board = ["X","X","X","","","","","",""]
    assert check_winner(board) == "X"


def test_check_winner_cols():
    board = ["O","","", "O","","","O","",""]
    assert check_winner(board) == "O"


def test_check_winner_diag():
    board = ["X","","", "","X","","","","X"]
    assert check_winner(board) == "X"


def test_check_winner_draw():
    board = ["X","O","X","X","O","O","O","X","X"]
    assert check_winner(board) == "draw"


def test_ai_move_block_win_medium():
    # medium AI should block player's immediate win
    board = ["X","X","", "","O","","","",""]
    move = ai_move(board, 'medium')
    assert move in (2,)


def test_ai_move_prefer_center_hard():
    board = ["","","", "","","","","",""]
    move = ai_move(board, 'hard')
    assert move == 4
