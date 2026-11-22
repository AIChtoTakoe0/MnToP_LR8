"""ЛР8, задание 4: asyncio — конкурентные «запросы» в одном потоке.

Три задачи ждут ответа по 1.0–2.0 с; await asyncio.sleep отдаёт управление,
поэтому общее время примерно равно самой долгой задаче (~2 с), а не сумме (4.5 с).
Запуск: python task4_asyncio/main.py
"""
import asyncio
import time


async def fetch(name: str, delay: float) -> str:
    """Имитация сетевого запроса: чистое ожидание, процессор не занят."""
    print(f"{time.strftime('%H:%M:%S')} | {name}: начало (ждём {delay} с)")
    await asyncio.sleep(delay)  # в этот момент выполняются остальные задачи
    print(f"{time.strftime('%H:%M:%S')} | {name}: готово")
    return f"{name} за {delay} с"


async def main() -> None:
    start = time.perf_counter()
    results = await asyncio.gather(       # запуск задач concurrently
        fetch("задача-1", 1.0),
        fetch("задача-2", 1.5),
        fetch("задача-3", 2.0),
    )
    elapsed = time.perf_counter() - start
    print("Результаты:", results)
    print(f"Общее время: {elapsed:.2f} с; последовательно было бы 4.50 с")
    assert elapsed < 3.0, "Задачи выполнялись последовательно — конкурентности нет"


if __name__ == "__main__":
    asyncio.run(main())
