import json
import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_move_invalid_board(client):
    # missing board
    res = client.post('/move', json={"index": 0, "level": "easy", "mode": "single"})
    assert res.status_code == 400


def test_move_invalid_index(client):
    # send invalid index
    board = ["", "", "", "", "", "", "", "", ""]
    res = client.post('/move', json={"index": 9, "board": board, "level": "easy", "mode": "single"})
    assert res.status_code == 400


def test_two_player_no_ai(client):
    # two-player: post a valid player move and ensure AI didn't play
    board = ["", "", "", "", "", "", "", "", ""]
    res = client.post('/move', json={"index": 0, "board": board, "mode": "two", "player": "X"})
    assert res.status_code == 200
    data = res.get_json()
    assert data['board'][0] == 'X'
    # no O played
    assert 'O' not in data['board'][1:]
