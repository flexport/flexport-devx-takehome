import json
import requests

URL = "http://0.0.0.0:5000"


def test_health():
    """
    Testing the /health endpoint
    """
    response = requests.get(f"{URL}/health")
    assert response.status_code == 200
    assert response.content == b"OK"

    print("OK")
