"""
Integration Testing during Kubernetes kind service deployment.
"""

import requests, os


def test_health():
    """testing health check function"""
    res = requests.get(os.environ.get("ENDPOINT", "http://localhost:7000") + "/health")
    assert res.content == b"OK"


def test_psr():
    """testing rps function"""
    res = requests.post(
        os.environ.get("ENDPOINT", "http://localhost:7000") + "/rps",
        json={"move": "rock"},
    )
    assert res.status_code == 200
