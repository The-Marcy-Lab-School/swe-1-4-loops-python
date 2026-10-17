import ast
import builtins
import inspect
import textwrap

from debug import broken_loop, broken_digit_count, broken_letter_count, broken_score_total

TEST_SUITE_NAME = "Debug Tests"


def code_used_in(func):
    """The kinds of code a function uses, and the names of the functions it calls.

    The function's code is read with Python's ast module rather than searched as
    text, so words in comments and strings never count. A comment that says
    "no if check needed" does not count as an if statement.
    """
    source = textwrap.dedent(inspect.getsource(func))
    kinds = set()
    for node in ast.walk(ast.parse(source)):
        kinds.add(type(node).__name__)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            kinds.add(node.func.id + "()")
    return kinds


def printed(capsys):
    return [line for line in capsys.readouterr().out.splitlines() if line.strip()]


def feed(monkeypatch, answers):
    """Stand in for a person typing, one answer per input() call."""
    supply = iter(answers)
    monkeypatch.setattr(builtins, "input", lambda *a: next(supply))


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


def test_broken_letter_count():
    """broken_letter_count - counts every time the letter appears, not only the last character"""
    assert broken_letter_count("banana", "a") == 3
    assert broken_letter_count("banana", "n") == 2
    assert broken_letter_count("mississippi", "s") == 4
    assert broken_letter_count("hello", "z") == 0


def test_broken_letter_count_empty_text():
    """broken_letter_count - returns 0 for empty text instead of crashing"""
    assert broken_letter_count("", "a") == 0


def test_broken_score_total_skips_bad_answers(monkeypatch, capsys):
    """broken_score_total - adds up the scores and skips answers that are not whole numbers"""
    feed(monkeypatch, ["90", "ten", "85", "done"])
    assert broken_score_total() == 175
    assert printed(capsys) == ["Sorry, ten is not a score"]

    feed(monkeypatch, ["ten", "9.5", "done"])
    assert broken_score_total() == 0
    assert printed(capsys) == ["Sorry, ten is not a score", "Sorry, 9.5 is not a score"]

    feed(monkeypatch, ["done"])
    assert broken_score_total() == 0


def test_broken_score_total_uses_continue(monkeypatch):
    """broken_score_total - uses a continue statement"""
    assert "Continue" in code_used_in(broken_score_total)

    feed(monkeypatch, ["70", "seventy", "done"])  # repeated to avoid an automatic pass
    assert broken_score_total() == 70
