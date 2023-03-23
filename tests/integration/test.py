import requests, os

def test_health():
	res = requests.get(os.environ["ENDPOINT"]+"/health")
	assert res.content == b"OK"

def test_rps():
	res = requests.post(os.environ["ENDPOINT"]+"/rps", json={"move": "rock"})
	assert res.status_code == 200