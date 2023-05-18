import pytest
from rock_paper_scissors.rps import rock_paper_scissors


def test_rps(mocker):
    """
    Basic test for Rock Paper Scissors
    """

    # When pc chooses rock move
    mocker.patch("rock_paper_scissors.rps.random.randint", return_value=0)

    game_result, pc_choice = rock_paper_scissors(0)
    assert game_result == 0
    assert pc_choice == 0

    game_result, pc_choice = rock_paper_scissors(1)
    assert game_result == 1
    assert pc_choice == 0

    game_result, pc_choice = rock_paper_scissors(2)
    assert game_result == -1
    assert pc_choice == 0

    # When pc chooses paper move
    mocker.patch("rock_paper_scissors.rps.random.randint", return_value=1)

    game_result, pc_choice = rock_paper_scissors(0)
    assert game_result == -1
    assert pc_choice == 1

    game_result, pc_choice = rock_paper_scissors(1)
    assert game_result == 0
    assert pc_choice == 1

    game_result, pc_choice = rock_paper_scissors(2)
    assert game_result == 1
    assert pc_choice == 1

    # When pc chooses scissor move
    mocker.patch("rock_paper_scissors.rps.random.randint", return_value=2)

    game_result, pc_choice = rock_paper_scissors(0)
    assert game_result == 1
    assert pc_choice == 2

    game_result, pc_choice = rock_paper_scissors(1)
    assert game_result == -1
    assert pc_choice == 2

    game_result, pc_choice = rock_paper_scissors(2)
    assert game_result == 0
    assert pc_choice == 2
