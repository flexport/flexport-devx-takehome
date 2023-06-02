"""
This module contains functional tests the rps app

Mostly just testing the flask API contract through local calls
"""
import json
import pytest
from rock_paper_scissors.app import app, mapping


def test_rps():
    """
    Test Flask Application and API for Rock Paper Scissors
    """
    with app.test_client() as test_client:
        response = test_client.post(
            "/rps", data=json.dumps({"move": "Rock"}), content_type="application/json"
        )
        assert response.status_code == 200


@pytest.mark.parametrize("move", mapping)
def test_rps_good_inputs(move):
    """
    Test Flask Application for the various valid inputs
    """
    with app.test_client() as test_client:
        response = test_client.post(
            "/rps", data=json.dumps({"move": move}), content_type="application/json"
        )
        assert response.status_code == 200


@pytest.mark.parametrize("bad_move", ["", "Dog", "123", "Rok"])
def test_rps_bad_inputs(bad_move):
    """
    Test Flask Application for invalid inputs
    """
    with app.test_client() as test_client:
        response = test_client.post(
            "/rps", data=json.dumps({"move": bad_move}), content_type="application/json"
        )
        message = response.data.decode("utf-8")
        assert response.status_code == 400
        assert message == f'"{bad_move}" is invalid. Valid moves: {mapping}'


def test_rps_no_input():
    """
    Test Flask Application for no json payload
    """
    with app.test_client() as test_client:
        response = test_client.post("/rps")
        assert response.status_code == 415


def test_rps_tie_message(mocker):
    """
    Test Flask Application to ensure a correct tie message

    PC: Rock
    Player: Rock
    """
    mocker.patch("rock_paper_scissors.rps.random.randint", return_value=0)
    move = "Rock"
    with app.test_client() as test_client:
        response = test_client.post(
            "/rps", data=json.dumps({"move": move}), content_type="application/json"
        )
        response_data = json.loads(response.data)
        assert response.status_code == 200
        assert isinstance(response_data, dict)
        result = response_data["result"]
        assert result == "Tie"


def test_rps_win_message(mocker):
    """
    Test Flask Application to ensure a correct win message

    PC: Rock
    Player: Paper
    """
    mocker.patch("rock_paper_scissors.rps.random.randint", return_value=0)
    move = "Paper"
    with app.test_client() as test_client:
        response = test_client.post(
            "/rps", data=json.dumps({"move": move}), content_type="application/json"
        )
        response_data = json.loads(response.data)
        assert response.status_code == 200
        assert isinstance(response_data, dict)
        result = response_data["result"]
        pc_choice = response_data["pc_choice"]
        assert result == f"You win, {move} beats {mapping[pc_choice]}"


def test_rps_lose_message(mocker):
    """
    Test Flask Application to ensure a correct lose message

    PC: Rock
    Player: Scissors
    """
    mocker.patch("rock_paper_scissors.rps.random.randint", return_value=0)
    move = "Scissors"
    with app.test_client() as test_client:
        response = test_client.post(
            "/rps", data=json.dumps({"move": move}), content_type="application/json"
        )
        response_data = json.loads(response.data)
        assert response.status_code == 200
        assert isinstance(response_data, dict)
        result = response_data["result"]
        pc_choice = response_data["pc_choice"]
        assert result == f"I win, {mapping[pc_choice]} beats {move}"


@pytest.mark.parametrize("move", ["rock", "Rock", "PAPER", "sCISSORs"])
def test_rps_capitalization(move):
    """
    Test Flask Application should handle variations in capitalization
    """
    with app.test_client() as test_client:
        response = test_client.post(
            "/rps", data=json.dumps({"move": move}), content_type="application/json"
        )
        assert response.status_code == 200


def test_rps_health_check():
    """
    Test Flask Application health
    """
    with app.test_client() as test_client:
        response = test_client.get("/health", content_type="application/json")
        message = response.data.decode("utf-8")
        assert response.status_code == 200
        assert message == "OK"
