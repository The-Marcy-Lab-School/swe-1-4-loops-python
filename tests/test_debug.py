from debug import broken_loop, broken_digit_count

TEST_SUITE_NAME = "Debug Tests"


def test_broken_loop():
    """broken_loop - builds a string from start (inclusive) to end (inclusive) by 1"""
    assert broken_loop(1, 10) == "12345678910"
    assert broken_loop(5, 12) == "56789101112"
    assert broken_loop(0, 0) == "0"
    assert broken_loop(0, -1) == ""


def test_broken_digit_count():
    """broken_digit_count - counts the digit characters in a string"""
    assert broken_digit_count("R2-D2") == 2
    assert broken_digit_count("2026-10-13") == 8
    assert broken_digit_count("no digits here") == 0
    assert broken_digit_count("") == 0
