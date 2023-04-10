"""
importing modules
"""
from rock_paper_scissors.rps import rock_paper_scissors


def test_rps():
    """
    Basic test for Rock Paper Scissors
    """

    assert rock_paper_scissors(1) is not None
    assert rock_paper_scissors(3) in [
        (-1, 1),
        (-1, 0),
        (-1, 2),
        (1, 0),
        (1, 1),
        (1, -1),
        (1, 2),
        (2, 1),
        (0, 1),
    ]
