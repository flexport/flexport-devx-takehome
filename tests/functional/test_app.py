import json
from rock_paper_scissors.app import app


def test_rps():
    """
    Test Flask Application and API for Rock Paper Scissors
    """
    with app.test_client() as test_client:
        response = test_client.get("/health")
        assert response.status_code == 200
        assert response.data.decode("utf-8") == "OK"

    with app.test_client() as test_client:
        response = test_client.post(
            "/rps", data=json.dumps({"move": "Rock"}), content_type="application/json"
        )
        assert response.status_code == 200

    with app.test_client() as test_client:
        response = test_client.post(
            "/rps", data=json.dumps({"move": "Paper"}), content_type="application/json"
        )
        assert response.status_code == 200

    with app.test_client() as test_client:
        response = test_client.post(
            "/rps",
            data=json.dumps({"move": "Scissors"}),
            content_type="application/json",
        )
        assert response.status_code == 200

    with app.test_client() as test_client:
        response = test_client.post(
            "/rps",
            data=json.dumps({"move": "dummyinvalidmove"}),
            content_type="application/json",
        )
        assert response.status_code != 200
