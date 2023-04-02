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


def test_rps_correct_cases():
    """
    Testing the /rps endpoint for all the possible cases for "Rock", "Paper" and "Scissors" game
    """
    mapping = ["Rock", "Paper", "Scissors"]

    for i in range(3):  # Test all possible cases
        all_results = set()
        all_pc_choices = set()
        while len(all_results) < 3 or len(all_pc_choices) < 3:
            headers = {"Content-type": "application/json"}
            response = requests.post(
                f"{URL}/rps", headers=headers, data=json.dumps({"move": mapping[i]})
            )
            assert response.status_code == 200

            obj = response.json()

            assert obj["game_result"] in [-1, 0, 1]
            assert obj["pc_choice"] in [0, 1, 2]
            all_results.add(obj["game_result"])
            all_pc_choices.add(obj["pc_choice"])

    print("OK")
