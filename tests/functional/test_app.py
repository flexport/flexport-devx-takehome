"""
   Copyright 2023 Flexport International, LLC

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
import json

from rock_paper_scissors.app import app


def test_health():
    """
    Testing the /health endpoint
    """
    with app.test_client() as test_client:
        res = test_client.get("/health")
        assert res.status_code == 200
        assert res.data == b"OK"


def test_rps_correct_cases():
    """
    Testing the /rps endpoint for all the possible cases for "Rock", "Paper" and "Scissors" game
    """

    with app.test_client() as test_client:
        mapping = ["Rock", "Paper", "Scissors"]

        for i in range(3):
            results = set()
            pc_choices = set()
            while len(results) < 3 or len(pc_choices) < 3:
                res = test_client.post(
                    "/rps",
                    data=json.dumps({"move": mapping[i]}),
                    content_type="application/json",
                )
                assert res.status_code == 200
                assert res.json["game_result"] in [-1, 0, 1]
                assert res.json["pc_choice"] in [0, 1, 2]
                results.add(res.json["game_result"])
                pc_choices.add(res.json["pc_choice"])


def test_rps_error_cases():
    """
    Test Flask Application and API for exception cases
    """
    invalid_moves = ["R ", "Sci", "P", ""]
    with app.test_client() as test_client:
        for move in invalid_moves:
            res = test_client.post(
                "/rps",
                data=json.dumps({"move": move}),
                content_type="application/json",
            )
            assert res.status_code == 500
