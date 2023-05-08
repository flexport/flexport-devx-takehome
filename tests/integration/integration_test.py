"""
Importing dependencies
"""

import os
import requests

URL = os.environ["URL"]


def test_health():  # pylint: disable=W3101
    """
    Testing the /health endpoint
    """
    response = requests.get(f"{URL}/health", timeout=60)
    assert response.status_code == 200
    assert response.content == b"OK"


def test_rps():
    """
    Testing deployed application for Rock Paper Scissors..
    """
    res = requests.post(URL + "/rps", json={"move": "rock"}, timeout=60)
    assert res.status_code == 200