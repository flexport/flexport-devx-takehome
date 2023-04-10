"""
Importing modules
"""
import json
from rock_paper_scissors.app import app


def test_rps():
    """
    Test Flask Application and API for Rock Paper Scissors..
    """
    with app.test_client() as test_client:
        moves = ["Rock", "Paper", "Scissors"]
        for move in moves:
            response = test_client.post(
                "/rps", data=json.dumps({"move": move}), content_type="application/json"
            )
            assert response.status_code == 200
        assert test_client.get("/health").data.decode("utf-8") == "OK"

        try:
            response = test_client.post(
                "/rps",
                data=json.dumps({"move": "wrong"}),
                content_type="application/json",
            )
        except ValueError:
            pass
