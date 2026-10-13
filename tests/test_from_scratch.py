import ast
import inspect
import textwrap

from from_scratch import (
    count_vowels,
    countdown_5_to_0,
    fizzbuzz,
    loop_0_up_to_10,
    loop_5_to_10,
    loop_even_numbers_up_to_10,
    loop_up_to_num,
    halving_steps,
)

TEST_SUITE_NAME = "From Scratch Tests"


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


def test_loop_0_up_to_10(capsys):
    """loop_0_up_to_10 - it prints from 0 (inclusive) to 10 (exclusive) by 1"""
    loop_0_up_to_10()
    assert printed(capsys) == [str(n) for n in range(10)]


def test_loop_5_to_10(capsys):
    """loop_5_to_10 - it prints from 5 (inclusive) to 10 (inclusive) by 1"""
    loop_5_to_10()
    assert printed(capsys) == ["5", "6", "7", "8", "9", "10"]


def test_loop_even_numbers_up_to_10(capsys):
    """loop_even_numbers_up_to_10 - it prints from 0 (inclusive) to 10 (exclusive) by 2"""
    loop_even_numbers_up_to_10()
    assert printed(capsys) == ["0", "2", "4", "6", "8"]


def test_loop_even_numbers_up_to_10_no_if(capsys):
    """loop_even_numbers_up_to_10 - does not rely on an if check or continue keyword"""
    used = code_used_in(loop_even_numbers_up_to_10)
    assert "If" not in used, "Count by 2 instead of checking each number with an if statement."
    assert "Continue" not in used

    loop_even_numbers_up_to_10()  # repeated to keep the test from auto-passing
    assert printed(capsys) == ["0", "2", "4", "6", "8"]


def test_countdown_5_to_0(capsys):
    """countdown_5_to_0 - it prints from 5 (inclusive) to 0 (inclusive) by -1"""
    countdown_5_to_0()
    assert printed(capsys) == ["5", "4", "3", "2", "1", "0"]


def test_loop_up_to_num(capsys):
    """loop_up_to_num - it prints from 0 (inclusive) to the given number (exclusive) by 1"""
    loop_up_to_num(5)
    assert printed(capsys) == ["0", "1", "2", "3", "4"]

    loop_up_to_num(3)
    assert printed(capsys) == ["0", "1", "2"]

    loop_up_to_num(0)
    assert printed(capsys) == []


def test_fizzbuzz(capsys):
    """fizzbuzz - it prints fizz, buzz, fizzbuzz, or the number correctly"""
    fizzbuzz()
    lines = printed(capsys)

    assert len(lines) == 100
    assert lines[0] == "1"
    assert lines[1] == "2"
    assert lines[2] == "fizz"
    assert lines[3] == "4"
    assert lines[4] == "buzz"
    assert lines[5] == "fizz"
    assert lines[9] == "buzz"
    assert lines[14] == "fizzbuzz"
    assert lines[29] == "fizzbuzz"
    assert lines[44] == "fizzbuzz"
    assert lines[59] == "fizzbuzz"
    assert lines[74] == "fizzbuzz"
    assert lines[89] == "fizzbuzz"
    assert lines[96] == "97"
    assert lines[99] == "buzz"


def test_count_vowels():
    """count_vowels - counts the vowels in a word"""
    assert count_vowels("hello") == 2
    assert count_vowels("rhythm") == 0
    assert count_vowels("AEIOU") == 5
    assert count_vowels("") == 0
    assert count_vowels("Programming") == 3


def test_count_vowels_with_y():
    """count_vowels - counts y as a vowel when asked"""
    assert count_vowels("rhythm", True) == 1
    assert count_vowels("hello", include_y=True) == 2
    assert count_vowels("YyY", include_y=True) == 3
    assert count_vowels("YyY") == 0


def test_halving_steps():
    """halving_steps - counts how many halvings bring a number below 1"""
    assert halving_steps(8) == 4
    assert halving_steps(1) == 1
    assert halving_steps(0.5) == 0
    assert halving_steps(0) == 0
    assert halving_steps(1024) == 11


def test_halving_steps_uses_while():
    """halving_steps - uses a while loop, since the count is not known up front"""
    used = code_used_in(halving_steps)
    assert "While" in used, "The number of halvings is not known in advance."
    assert "range()" not in used
