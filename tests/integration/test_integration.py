import requests

def test_health():
    """
    Health Check for Rock Paper Scissors Application
    """
    resp = requests.get("http://127.0.0.1:5000/health")
    assert resp.status_code == 200


def test_game():
    """
    Test the Rock Paper Scissors Game Play
    """
    payload = '{"move": "Rock"}'
    headers = {"Content-Type": "application/json"}
    resp = requests.post("http://127.0.0.1:8000/rps", data=payload, headers=headers)
    assert resp.status_code == 200
    pc_choice, game_result, result = resp.json()['pc_choice'], resp.json()['game_result'], resp.json()['result']
    if pc_choice == 0:
        assert game_result == 0
        assert result == "Tie"
    elif pc_choice == 1:
        assert game_result == -1
        assert result == "I win, Paper beats Rock"
    else:
        assert game_result == 1
        assert result == "You win, Rock beats Scissors"

test_game()