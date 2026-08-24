num1_str = input("Введите первое число: ")

if num1_str.replace('.', '', 1).replace('-', '', 1).isdigit():
    num1 = float(num1_str)
else:
    print("Ошибка: первое число введено некорректно.")
    exit()

num2_str = input("Введите второе число: ")

if num2_str.replace('.', '', 1).replace('-', '', 1).isdigit():
    num2 = float(num2_str)
else:
    print("Ошибка: второе число введено некорректно.")
    exit()

operator = input("Выберите оператор (+, -, *, /): ")

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 == 0:
        print("Ошибка: деление на ноль.")
        exit()
    result = num1 / num2
else:
    print("Ошибка: неверный оператор.")
    exit()

print(f"Результат: {num1} {operator} {num2} = {result}")