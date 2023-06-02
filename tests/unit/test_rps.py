"""
This module contains unit tests the rps app

Testing individual functions and their parameters
"""
import pytest
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
    gr, _ = rock_paper_scissors(0)
    assert gr == 0
    # PC: Rock, User: Paper
    gr, _ = rock_paper_scissors(1)
    assert gr == 1
    # PC: Rock, User: Scissors
    gr, _ = rock_paper_scissors(1)
    assert gr == -1
    mocker.patch("rock_paper_scissors.rps.random.randint", return_value=1)
    # PC: Paper, User: Rock
    gr, _ = rock_paper_scissors(0)
    assert gr == -1
    # PC: Paper, User: Paper
    gr, _ = rock_paper_scissors(1)
    assert gr == 0
    # PC: Paper, User: Scissors
    gr, _ = rock_paper_scissors(1)
    assert gr == 1
    mocker.patch("rock_paper_scissors.rps.random.randint", return_value=2)
    # PC: Scissors, User: Rock
    gr, _ = rock_paper_scissors(0)
    assert gr == 1
    # PC: Scissors, User: Paper
    gr, _ = rock_paper_scissors(1)
    assert gr == -1
    # PC: Scissors, User: Scissors
    gr, _ = rock_paper_scissors(1)
    assert gr == 0
