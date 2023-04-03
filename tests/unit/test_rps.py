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
from rock_paper_scissors.rps import rock_paper_scissors


def test_rps():
    """
    Testing for all the possible cases for "Rock", "Paper" and "Scissors" game
    """
    for i in range(3):
        results = set()
        pc_choices = set()
        while len(results) < 3 or len(pc_choices) < 3:
            result, pc_choice = rock_paper_scissors(i)
            assert result in [-1, 0, 1]
            assert pc_choice in [0, 1, 2]
            results.add(result)
            pc_choices.add(pc_choice)
