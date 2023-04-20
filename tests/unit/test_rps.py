from rock_paper_scissors.rps import rock_paper_scissors


def test_rps():
    """
    Basic test for Rock Paper Scissors
    """

    # 0 = Rock, 1 = Paper, 2 = Scissors

    # Test Not None
    assert rock_paper_scissors(0) is not None
    assert rock_paper_scissors(1) is not None
    assert rock_paper_scissors(2) is not None

    # Check if User picks rock
    result, pc_choice = rock_paper_scissors(0)
    assert (
        (result == 0 and pc_choice == 0)
        or (result == 1 and pc_choice == 2)
        or (result == -1 and pc_choice == 1)
    )

    # Check if User picks paper
    result, pc_choice = rock_paper_scissors(1)
    assert (
        (result == 0 and pc_choice == 1)
        or (result == 1 and pc_choice == 0)
        or (result == -1 and pc_choice == 2)
    )

    # Check if User picks scissors
    result, pc_choice = rock_paper_scissors(2)
    assert (
        (result == 0 and pc_choice == 2)
        or (result == 1 and pc_choice == 1)
        or (result == -1 and pc_choice == 0)
    )
