# Исходная необработанная строка из источника данных
raw_user_record = " 10827 ; aLeXanDer_vLaDimiRov ; mInSk ; ACTIVE "

# Разбил строку на элементы по разделителю ';'
parts = raw_user_record.split(";")

# Убрал лишние пробелы по краям каждого элемента
parts = [part.strip() for part in parts]

# Добавил префикс UID- к идентификатору через f-строку
user_id = f"UID-{parts[0]}"

# Заменил '_' на пробел в имени и сделал каждое слово с заглавной буквы
user_name = parts[1].replace("_", " ").title()

# Перевёл город в верхний регистр
city = parts[2].upper()

# Перевёл статус в нижний регистр
status = parts[3].lower()

# Собрал всё в одну строку с разделителем '|'
normalized_record = " | ".join([user_id, user_name, city, status])

print(f"Нормализованная запись: {normalized_record}")