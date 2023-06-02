"""
This file will test a deployed flask application on k8s and send requests
over the loopback address
"""
import requests
from rock_paper_scissors.app import mapping

url = 'localhost:5000'
def test_rps_health():
    response = requests.post(url + "/health")
    assert response.status_code == 200
    assert response.text == "OK"

def test_rps_basic():
    payload = {'move': 'Rock'}
    response = requests.post(url + "/rps", json=payload)
    assert response.status_code == 200
    response = response.json()
    assert isinstance(response, dict)
    assert "result" in response
    assert "game_result" in response
    assert "pc_choice" in response

def test_rps_bad_payload():
    move = "invalid_move"
    payload = {'move': move}
    response = requests.post(url + "/rps", json=payload)
    assert response.status_code == 400
    assert response.text == f"\"{move}\" is invalid. Valid moves: {mapping}"

def test_rps_no_payload():
    response = requests.post(url + "/rps")
    assert response.status_code == 400
    assert response.text == f"\"\" is invalid. Valid moves: {mapping}"
