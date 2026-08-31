MAX_RENTAL_BATCH_LIMIT = 150.0


def calculate_rental_batch(quantity: int, rental_rate: float,
                           discount: float = 0.0) -> tuple[float, bool]:
    """Рассчитывает стоимость партии дисков с учётом жанровой скидки.

    Args:
        quantity: количество дисков в партии;
        rental_rate: цена аренды одного диска в долларах;
        discount: скидка долей (0.1 = 10%).

    Returns:
        Кортеж (final_sum, is_limit_exceeded): округлённая стоимость партии и флаг превышения лимита."""
    # Посчитал итоговую сумму со скидкой и округлил до 2 знаков
    final_sum = round(quantity * rental_rate * (1 - discount), 2)
    # Вернул кортеж: сумма и флаг превышения лимита
    return final_sum, final_sum > MAX_RENTAL_BATCH_LIMIT


print("=== ОТЧЁТ ПО ПАРТИЯМ АРЕНДЫ ===")

# Партия 1: вызвал функцию с позиционными аргументами, без скидки
total, exceeded = calculate_rental_batch(30, 2.99)
print(f"Партия 1 (Academy Dinosaur): Сумма {total}$. Превышение лимита: {exceeded}")

# Партия 2: вызвал с именованными аргументами, скидка 10%
total, exceeded = calculate_rental_batch(quantity=40, rental_rate=4.99, discount=0.10)
print(f"Партия 2 (Affair Prejudice): Сумма {total}$. Превышение лимита: {exceeded}")

# Партия 3: вызвал функцию с позиционными аргументами
total, exceeded = calculate_rental_batch(10, 1.99)
print(f"Партия 3 (Agent Truman): Сумма {total}$. Превышение лимита: {exceeded}")

# Партия 4: вызвал функцию с именованными аргументами, скидка 20%
total, exceeded = calculate_rental_batch(quantity=50, rental_rate=3.50, discount=0.20)
print(f"Партия 4 (African Egg): Сумма {total}$. Превышение лимита: {exceeded}")