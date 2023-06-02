"""
This module contains unit tests the rps app

Testing individual functions and their parameters
"""
from rock_paper_scissors.rps import rock_paper_scissors


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


def test_rps_game_result(mocker):
    """
    Test that Rock Paper Scissors returns correct game result values
    """
    mocker.patch("rock_paper_scissors.rps.random.randint", return_value=0)
    # PC: Rock, User: Rock
    res, _ = rock_paper_scissors(0)
    assert res == 0
    # PC: Rock, User: Paper
    res, _ = rock_paper_scissors(1)
    assert res == 1
    # PC: Rock, User: Scissors
    res, _ = rock_paper_scissors(2)
    assert res == -1
    mocker.patch("rock_paper_scissors.rps.random.randint", return_value=1)
    # PC: Paper, User: Rock
    res, _ = rock_paper_scissors(0)
    assert res == -1
    # PC: Paper, User: Paper
    res, _ = rock_paper_scissors(1)
    assert res == 0
    # PC: Paper, User: Scissors
    res, _ = rock_paper_scissors(2)
    assert res == 1
    mocker.patch("rock_paper_scissors.rps.random.randint", return_value=2)
    # PC: Scissors, User: Rock
    res, _ = rock_paper_scissors(0)
    assert res == 1
    # PC: Scissors, User: Paper
    res, _ = rock_paper_scissors(1)
    assert res == -1
    # PC: Scissors, User: Scissors
    res, _ = rock_paper_scissors(2)
    assert res == 0
