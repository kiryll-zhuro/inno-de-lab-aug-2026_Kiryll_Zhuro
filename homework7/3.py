# Конфигурационный словарь, полученный от сервиса инициализации
db_config = {
    "connection": {
        "host": "production-db.internal",
        "port": 5432,
        "user": "postgres"
    }
}

# Достал вложенный словарь connection, из него host и port через .get() с запасными значениями
connection = db_config.get("connection", {})
host = connection.get("host", "localhost")
port = connection.get("port", 5432)

# Безопасно проверил наличие ssl_settings и ssl_mode:
# если их нет, подставится дефолт verify-full
ssl_mode = db_config.get("ssl_settings", {}).get("ssl_mode", "verify-full")
print(f"SSL Mode: {ssl_mode}")

# Поменял пользователя на admin
connection["user"] = "admin"

# Добавил новый параметр max_connections, равный 100
connection["max_connections"] = 100

print("Параметры соединения:")
for key, value in connection.items():
    print(f"* {key}: {value}")