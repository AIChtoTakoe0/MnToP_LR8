"""ЛР8, задание 1: модуль logging — уровни, формат, вывод в консоль и файл.

Запуск: python task1_logging/main.py
Журнал: консоль получает INFO и выше; файл app.log — все уровни (включая DEBUG).
"""
import logging
from pathlib import Path

LOG_FILE = Path(__file__).resolve().parent / "app.log"

# Логгер приложения; имя принято брать из __name__ (здесь: "__main__")
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # логгер не фильтрует; фильтруют обработчики

# Обработчик 1: консоль, только INFO и выше
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(logging.Formatter(
    "%(asctime)s | %(levelname)-8s | %(message)s", datefmt="%H:%M:%S"))
logger.addHandler(console)

# Обработчик 2: файл, все уровни — полный журнал
file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter(
    "%(asctime)s | %(levelname)-8s | %(funcName)s | %(message)s"))
logger.addHandler(file_handler)


def divide(a: float, b: float) -> float:
    """Деление с журналированием каждого шага."""
    logger.debug("divide: получены a=%s, b=%s", a, b)    # DEBUG — только в файл
    if b == 0:
        logger.error("Деление на ноль: a=%s, b=%s", a, b)
        raise ZeroDivisionError("b не должно быть равно 0")
    result = a / b
    logger.info("divide: %s / %s = %s", a, b, result)    # параметры подставляет logging — без f-строки
    return result


if __name__ == "__main__":
    logger.warning("Запуск демонстрации logging")            # WARNING — виден в консоли
    divide(10, 2)
    try:
        divide(5, 0)
    except ZeroDivisionError:
        logger.exception("Перехвачена ошибка деления")       # logger.exception добавляет traceback
