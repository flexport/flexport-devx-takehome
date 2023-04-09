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
        response = requests.post(f"{URL}/rps", data={"move": move})
        assert response.status_code == 200

    try:
        response = requests.post("/rps", data={"move": "wrong"})
    except ValueError:
        pass
