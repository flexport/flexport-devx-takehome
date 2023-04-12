import json
import requests

URL = "http://127.0.0.1:5000"

def test_health():
    """
    Testing the /health endpoint
    """
    response = requests.get(f"{URL}/health")
    assert response.status_code == 200
    assert response.content == b"OK"

def test_rps_with_valid_input():
    """
    Testing the /rps with valid input post request
    """
    data = {"move": "Rock"}
    response = requests.post(f"{URL}/rps", json=data)
    assert response.status_code == 200

    data = {"move": "Paper"}
    response = requests.post(f"{URL}/rps", json=data)
    assert response.status_code == 200

    data = {"move": "Scissors"}
    response = requests.post(f"{URL}/rps", json=data)
    assert response.status_code == 200

def test_rps_with_invalid_input():
    """
    Testing the /rps with invalid input post request
    """
    data = {"move": "Papers"}
    response = requests.post(f"{URL}/rps", json=data)
    assert response.status_code == 500
