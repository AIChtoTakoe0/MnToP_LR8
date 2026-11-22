"""ЛР8, задание 3: простые функции для демонстрации pytest (pytest — тесты рядом в test_math_utils.py)."""


def factorial(n: int) -> int:
    """Факториал целого неотрицательного числа."""
    if isinstance(n, bool) or not isinstance(n, int) or n < 0:
        raise ValueError("n должно быть целым неотрицательным числом")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_palindrome(text: str) -> bool:
    """True, если строка читается одинаково в обе стороны (регистр и небуквенные символы не учитываются)."""
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]
