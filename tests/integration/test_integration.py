"""
Tests for When RPS App is running
"""

import requests

RPS_HOST = "http://127.0.0.1:5000"


def check_result(user_choice, pc_choice, result, game_outcome):
    """
    Checks result of game for when RPS App is running
    """
    if game_outcome == -1:
        assert result == f"I win, {pc_choice} beats {user_choice}"
    elif game_outcome == 0:
        assert result == "Tie"
    elif game_outcome == -1:
        assert result == f"You win, {user_choice} beats {pc_choice}"


def test_endpoints():
    """
    Tests All Endpoints for when RPS App is running
    """
    # Health Check
    health_reponse = requests.get(f"{RPS_HOST}/health")
    assert health_reponse.status_code == 200
    assert health_reponse.content == b"OK"

    # Check Invalid Option
    invalid_response = requests.post(
        f"{RPS_HOST}/rps", json={"move": "dummyinvalidmove"}
    )
    assert invalid_response.status_code != 200

    # Check Options
    for option in ["Rock", "Paper", "Scissors"]:
        app_response = requests.post(f"{RPS_HOST}/rps", json={"move": option})
        assert app_response.status_code == 200
        data = app_response.json()
        pc_choice = data["pc_choice"]
        game_outcome = data["game_result"]
        result = data["result"]
        check_result(option, pc_choice, game_outcome, result)
