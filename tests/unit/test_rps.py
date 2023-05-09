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
    Basic test for Rock Paper Scissors
    """

    assert rock_paper_scissors(1) is not None
    assert rock_paper_scissors(100000) is not None
    assert rock_paper_scissors(98765) is not None
    assert rock_paper_scissors(3) in [(0,1), (2,1), (-1, 1),(-1, 0),(1, 2),(-1, 2),(1, 0),(1, 1),(1, -1)]
