import json

from rock_paper_scissors.app import app


def test_health():
    """
    Test Flask Application and API for health
    """

    with app.test_client() as test_client:
        response = test_client.get('/health')

        assert response.status_code == 200
        assert response.data == b'OK'


def test_rps():
    """
    Test Flask Application and API for Rock Paper Scissors
    """
    with app.test_client() as test_client:
        response = test_client.post(
            '/rps',
            data=json.dumps(dict(move='Rock')),
            content_type='application/json',
        )
        assert response.status_code == 200


def test_rps_invalid_move():
    """
    Test exception in Flask Application's rps function
    """
    with app.test_client() as test_client:
        response = test_client.post(
            '/rps',
            data=json.dumps(dict(move='hello')),
            content_type='application/json',
        )
        assert response.status_code == 500