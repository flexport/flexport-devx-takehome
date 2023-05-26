from rock_paper_scissors.rps import rock_paper_scissors


def test_rps():
    """
    Basic test for Rock Paper Scissors
    """

    assert rock_paper_scissors(1) is not None

def test_rps():
    """
    Basic test for Rock Paper Scissors
    """

    assert rock_paper_scissors(1)[0] in (0, -1, 1)
    assert rock_paper_scissors(1)[1] in (0, -1, 1)
