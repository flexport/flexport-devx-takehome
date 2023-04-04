"""
    This module contains unit tests for the rock-paper-scissors game.
"""

from rock_paper_scissors.rps import rock_paper_scissors


def test_rps():
    """
    Test the `rock_paper_scissors()` function by calling it with an input value of 1,
    and ensuring that the function returns a non-None value.
    """

    assert rock_paper_scissors(1) is not None


def test_rps_valid_input():
    """
    Test rock paper scissors function with valid inputs.
    The function should return one of three possible values:
    - 0 for a tie
    - 1 for a player win
    - -1 for a computer win
    """

    # Testing all valid user inputs (0, 1, 2)
    for user_input in range(3):
        result, pc_choice = rock_paper_scissors(user_input)
        # Ensure that the function returns an integer value
        assert isinstance(result, int)
        assert isinstance(pc_choice, int)
        # Check that the returned values match the expected results for all possible outcomes
        if user_input == pc_choice:
            assert result == 0
        elif (user_input + 1) % 3 == pc_choice % 3:
            assert result == -1
        else:
            assert result == 1
