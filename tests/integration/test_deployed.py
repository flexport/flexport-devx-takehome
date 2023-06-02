"""
This file will test a deployed flask application on k8s and send requests
over the loopback address
"""
import requests
from rock_paper_scissors.app import mapping


def request_deployment(endpoint, payload=None, get=False):
    """
    Helper function for pinging a deployed service
    """
    url = "http://localhost:5000"
    if get:
        return requests.get(url + "/" + endpoint, timeout=5)
    return requests.post(url + "/" + endpoint, json=payload, timeout=5)


def test_rps_health():
    """
    Test health check
    """
    response = request_deployment("health", get=True)
    assert response.status_code == 200
    assert response.text == "OK"


def test_rps_basic():
    """
    Test a basic query
    """
    payload = {"move": "Rock"}
    response = request_deployment("rps", payload)
    assert response.status_code == 200
    response = response.json()
    assert isinstance(response, dict)
    assert "result" in response
    assert "game_result" in response
    assert "pc_choice" in response


def test_rps_bad_payload():
    """
    Test an invalid move
    """
    move = "invalid_move"
    payload = {"move": move}
    response = request_deployment("rps", payload)
    assert response.status_code == 400
    assert response.text == f'"{move}" is invalid. Valid moves: {mapping}'


def test_rps_no_payload():
    """
    Test without payload supplied
    """
    response = request_deployment("rps")
    assert response.status_code == 415


def test_rps_wrong_method():
    """
    Test calling GET request on rps but rps is POST only
    """
    response = request_deployment("rps", get=True)
    assert response.status_code == 405
