import time
from typing import Any, Callable

PERFORMANCE_LOG_PREFIX = "[PERF_LOG]"
TIME_DECIMALS = 8


def performance_logger(func: Callable[..., Any]) -> Callable[..., Any]:
    """Декоратор, который замеряет время выполнения функции.

    Args:
        func: целевая функция, которую оборачиваем.

    Returns:
        Обёртка, которая логирует время выполнения и возвращает результат оригинальной функции."""
    # Обёртка принимает любые позиционные и именованные аргументы
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Зафиксировал время начала
        start = time.perf_counter()
        # Выполнил оригинальную функцию с переданными аргументами
        result = func(*args, **kwargs)
        # Посчитал время работы и округлил до TIME_DECIMALS знаков
        elapsed = round(time.perf_counter() - start, TIME_DECIMALS)
        # Вывел лог с префиксом и именем функции
        print(f"{PERFORMANCE_LOG_PREFIX} Функция '{func.__name__}' выполнена за {elapsed} секунд.")
        # Вернул результат оригинальной функции
        return result

    return wrapper


@performance_logger
def get_sorted_report(revenue: list[dict[str, str | float]]) -> list[dict[str, str | float]]:
    """Сортирует выручку жанров по убыванию.

    Args:
        revenue: список словарей с данными по выручке жанров.

    Returns:
        Список, отсортированный по убыванию total_sales."""
    # Отсортировал через sorted() с lambda по ключу total_sales по убыванию
    return sorted(revenue, key=lambda item: item["total_sales"], reverse=True)


print("=== ТЕСТИРОВАНИЕ ПРОИЗВОДИТЕЛЬНОСТИ ===")

# Тестовые наборы данных
datasets = [
    [
        {"category": "Action", "total_sales": 4311.85},
        {"category": "Animation", "total_sales": 4656.30},
        {"category": "Children", "total_sales": 3655.55},
    ],
    [
        {"category": "Classics", "total_sales": 1200.10},
        {"category": "Comedy", "total_sales": 4000.00},
        {"category": "Documentary", "total_sales": 4000.00},
    ],
    [
        {"category": "Drama", "total_sales": 500.00},
    ],
]

# Прогнал тесты в цикле и вывел топ категорий по выручке
for test_number, data in enumerate(datasets, start=1):
    print(f"--- ТЕСТ {test_number} ---")
    report = get_sorted_report(data)
    print("Топ категорий по выручке:")
    for position, item in enumerate(report, start=1):
        print(f"{position}. {item['category']}: {item['total_sales']}")