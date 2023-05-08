"""
Importing dependencies
"""

import os
import requests

URL = os.environ["URL"]


def test_health(): 
    """
    Test the /health endpoint
    """
    response = requests.get(f"{URL}/health", timeout=60)
    assert response.status_code == 200
    assert response.content == b"OK"


def test_rps():
    """
    Test deployed application
    """
    res = requests.post(URL + "/rps", json={"move": "rock"}, timeout=60)
    assert res.status_code == 200