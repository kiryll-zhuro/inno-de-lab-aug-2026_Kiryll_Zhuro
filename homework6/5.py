import random

secret = random.randint(1, 20)
attempts = 5

print(f"Я загадал число от 1 до 20. У тебя {attempts} попыток!")

while attempts > 0:
    guess = int(input(f"Попытка {6 - attempts}. Введите число: "))
    attempts -= 1

    if guess == secret:
        print("Ты угадал! Отличная работа.")
        break
    elif guess > secret:
        print(f"Слишком много! Осталось попыток: {attempts}")
    else:
        print(f"Слишком мало! Осталось попыток: {attempts}")
else:
    print(f"Попытки закончились. Было загадано число {secret}.")