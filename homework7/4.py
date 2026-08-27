# Список ролей, переданный в запросе на авторизацию (содержит повторы)
requested_roles = ["guest", "developer", "guest", "admin",
                   "developer", "guest"]

# Набор обязательных ролей для выполнения административных функций
required_admin_roles = {"admin", "security_officer", "audit_manager"}

# Превратил список во множество, чтобы сразу убрать дубликаты
unique_requested = set(requested_roles)

# С помощью пересечения нашёл роли, которые есть и в запросе, и в обязательных
common_admin_roles = unique_requested & required_admin_roles

# С помощью разности нашёл обязательные роли, которых не было в запросе
missing_admin_roles = required_admin_roles - unique_requested

# Проверил через in, есть ли security_officer в запросе
has_security_officer = "security_officer" in unique_requested

print(f"Уникальные запрошенные роли: {unique_requested}")
print(f"Общие административные роли: {common_admin_roles}")
print(f"Недостающие административные роли: {missing_admin_roles}")
print(f"Наличие роли security_officer в запросе: {has_security_officer}")