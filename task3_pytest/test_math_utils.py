"""ЛР8, задание 3: тесты pytest для math_utils.py.

Запуск: cd task3_pytest && python -m pytest -v
"""
import pytest

from math_utils import factorial, is_palindrome


def test_factorial_of_zero():
    assert factorial(0) == 1


def test_factorial_of_five():
    assert factorial(5) == 120


@pytest.mark.parametrize("n, expected", [(1, 1), (3, 6), (6, 720)])
def test_factorial_table(n, expected):
    assert factorial(n) == expected


def test_factorial_negative_raises():
    with pytest.raises(ValueError):
        factorial(-1)


@pytest.mark.parametrize(
    "text, expected",
    [
        ("казак", True),
        ("А роза упала на лапу Азора", True),
        ("python", False),
    ],
)
def test_is_palindrome(text, expected):
    assert is_palindrome(text) == expected
