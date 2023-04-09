import requests
import os
import json

URL = os.environ["URL"]


def test_health():
    """
    Testing the /health endpoint
    """
    response = requests.get(f"{URL}/health")
    assert response.status_code == 200
    assert response.content == b"OK"


def test_rps():
    """
    Testing deployed application for Rock Paper Scissors..
    """
    moves = ["Rock", "Paper", "Scissors"]
    for move in moves:
        response = requests.post(URL + "/rps", json=json.dumps({"move": move}))
        assert response.status_code == 200
        assert requests.get(URL + "/health").data.decode("utf-8") == "OK"

    try:
        response = requests.post("/rps", data=json.dumps({"move": "wrong"}))
    except ValueError:
        pass
