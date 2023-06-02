"""
This module contains unit tests the rps app

Testing individual functions and their parameters
"""
from rock_paper_scissors.rps import rock_paper_scissors
from rock_paper_scissors.app import health

def test_rps():
    """
    Basic test for Rock Paper Scissors
    """

    assert rock_paper_scissors(1) is not None

def test_rps_inputs():
    """
    Test that Rock Paper Scissors inputs are all accepted
    """
    for choice in range(3):
        assert rock_paper_scissors(choice) is not None

def test_rps_game_result():
    """
    Test that Rock Paper Scissors returns correct game result values
    """
    # find one result of each: 0, -1, 1
    found = [False for _ in range(3)]
    while not all(found):
        res = rock_paper_scissors(1)[0]
        found[res] = True
        assert res in (-1, 0, 1)

def test_rps_pc_choice():
    # find one result of each: 0, 1, 2
    while not all(found):
        res = rock_paper_scissors(1)[1]
        found[res] = True
        assert res in (0, 1, 2)
