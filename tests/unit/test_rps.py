import unittest
from unittest.mock import patch
from rock_paper_scissors.rps import rock_paper_scissors


@patch('random.randint')
def test_rps(randint):
    """
    Basic test for Rock Paper Scissors
    """
    # pc: 0, user:0, --> 0,0
    randint.return_value = 0
    assert rock_paper_scissors(0) == (0, 0)
    # pc: 1, user:0,
    randint.return_value = 1
    assert rock_paper_scissors(0) == (-1, 1)
    # pc: 2, user:0,
    randint.return_value = 2
    assert rock_paper_scissors(0) == (1, 2)


