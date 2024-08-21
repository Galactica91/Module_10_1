import datetime

now = datetime.datetime.now()

print("Текущая дата и время:", now)

# Вывод в разных форматах:
print("Дата:", now.strftime("%Y-%m-%d"))
print("Время:", now.strftime("%H:%M:%S"))
print("Полный формат:", now.strftime("%Y-%m-%d %H:%M:%S"))