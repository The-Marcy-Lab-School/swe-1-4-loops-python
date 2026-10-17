import ast
import inspect
import textwrap

from modify import while_to_for

TEST_SUITE_NAME = "Modify Tests"


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


def test_while_to_for_no_longer_uses_while():
    """while_to_for - no longer uses a while loop"""
    used = code_used_in(while_to_for)
    assert "While" not in used
    assert "For" in used


def test_while_to_for_output(capsys):
    """while_to_for - it prints from 0 (inclusive) to 5 (exclusive) by 1"""
    used = code_used_in(while_to_for)  # repeated to avoid an automatic pass
    assert "While" not in used
    assert "For" in used

    while_to_for()
    assert printed(capsys) == ["0", "1", "2", "3", "4"]

