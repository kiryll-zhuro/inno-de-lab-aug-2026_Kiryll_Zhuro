from typing import Any

DEFAULT_RETURN_INDEX_BASE = 10.0


def calculate_overdue_fine(title: str, days_overdue: Any,
                           fine_rate: float) -> tuple[float, float] | None:
    """Рассчитывает штраф и индекс оборачиваемости возврата.

    Args:
        title: название фильма,
        days_overdue: сырые данные о днях просрочки (число или строка),
        fine_rate: штраф за один день просрочки.

    Returns:
        Кортеж (total_fine, return_index) при успехе или None, если входные данные некорректны.

    Функция обрабатывает ошибки входных данных:
        TypeError — данные вообще нельзя преобразовать к float;
        ValueError — строка не содержит числа;
        ZeroDivisionError — деление на ноль."""
    try:
        # Преобразовал дни просрочки к float
        numeric_days = float(days_overdue)
        # Посчитал итоговый штраф
        total_fine = numeric_days * fine_rate
        # Посчитал индекс оборачиваемости
        return_index = DEFAULT_RETURN_INDEX_BASE / numeric_days
        # Вывел успешный результат
        print(f"Фильм: '{title}' | Итоговый штраф: {total_fine}$ | Индекс: {return_index}")
        return total_fine, return_index
    except TypeError as error:
        # Данные нельзя преобразовать в число
        print(f"[ОШИБКА ТИПА] Некорректный тип данных для '{title}': {error}")
    except ValueError as error:
        # Строка не содержит числа
        print(f"[ОШИБКА ЗНАЧЕНИЯ] Невозможно преобразовать дни в число для '{title}': {error}")
    except ZeroDivisionError as error:
        # Деление на ноль
        print(f"[ОШИБКА ДЕЛЕНИЯ НА НОЛЬ] Возврат без просрочки для '{title}': {error}")
    finally:
        # Этот блок выполняется всегда
        print("--- Проверка транзакции возврата завершена ---")
    return None


print("=== ПРОВЕРКА ВОЗВРАТОВ ===")

# Прогнал проверки: один успех и три разные ошибки
calculate_overdue_fine("Matrix", 5, 1.5)
calculate_overdue_fine("Inception", "пять", 2.0)
calculate_overdue_fine("Avatar", 0, 2.5)
calculate_overdue_fine("Interstellar", [3], 3.0)