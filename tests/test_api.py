import json
import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client



def test_move_invalid_index(client):
    # send invalid index (out of range)
    client.post('/start', json={"mode": "single", "level": "easy"})
    res = client.post('/move', json={"index": 9})
    assert res.status_code == 400



def test_move_on_filled_cell(client):
    # start game, make a move, then try to move again in same cell
    client.post('/start', json={"mode": "single", "level": "easy"})
    res1 = client.post('/move', json={"index": 0})
    assert res1.status_code == 200
    res2 = client.post('/move', json={"index": 0})
    assert res2.status_code == 400


def test_two_player_no_ai(client):
    # two-player: start game, alternate moves, ensure no AI
    client.post('/start', json={"mode": "two"})
    res1 = client.post('/move', json={"index": 0})
    assert res1.status_code == 200
    data1 = res1.get_json()
    assert data1['board'][0] == 'X'
    res2 = client.post('/move', json={"index": 1})
    assert res2.status_code == 200
    data2 = res2.get_json()
    assert data2['board'][1] == 'O'
    # no AI move: only one cell filled per move
    assert data2['board'].count('O') == 1
