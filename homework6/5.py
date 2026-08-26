import random

MIN_NUMBER = 1
MAX_NUMBER = 20
MAX_ATTEMPTS = 5

secret = random.randint(MIN_NUMBER, MAX_NUMBER)
attempts = MAX_ATTEMPTS

print(f"Я загадал число от {MIN_NUMBER} до {MAX_NUMBER}. У тебя {attempts} попыток!")

while attempts > 0:
    guess = int(input(f"Попытка {MAX_ATTEMPTS - attempts + 1}. Введите число: "))
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