from logic_utils import check_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


def test_win_score_uses_attempt_number():
    # Winning with fewer attempts should give a higher score.
    first_attempt_score = update_score(0, "Win", 1)
    fourth_attempt_score = update_score(0, "Win", 4)

    assert first_attempt_score > fourth_attempt_score
