# Список транзакций, полученных от платёжного шлюза
raw_transactions = ["SUCCESS:100", "FAILED:50", "SUCCESS:-10",
                    "SUCCESS:0", "SUCCESS:250", "ERROR:200"]

# Отфильтровал в одну строку: оставил только SUCCESS,
# достал сумму после двоеточия, превратил в целые числа, 
# отбросил суммы меньше или равные 0
clean_transactions = [int(tx.split(":")[1]) for tx in raw_transactions if tx.split(":")[0] == "SUCCESS" and int(tx.split(":")[1]) > 0]

print(f"Очищенные транзакции: {clean_transactions}")