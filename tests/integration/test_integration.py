"""
Integration Testing during Kubernetes kind service deployment.
"""

import requests, os


def test_health():
    """testing health check function"""
    res = requests.get(os.environ["ENDPOINT"] + "/health")
    assert res.content == b"OK"


def test_psr():
    """testing rps function"""
    if "USER" not in os.environ:
        "ENDPOINT" = "http://localhost:5000"
    res = requests.post(os.environ["ENDPOINT"] + "/rps", json={"move": "rock"})
    assert res.status_code == 200
