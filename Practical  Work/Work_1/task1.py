# Ввод количества имен
N = int(input("Введите количество имен: "))

# Ввод имен в список
names = []
for _ in range(N):
    name = input("Введите имя: ")
    names.append(name)

# Создание списка uni с уникальными длинами
uni = []
lengths = set()  # Множество для отслеживания использованных длин

for name in names:
    if len(name) not in lengths:
        uni.append(name)
        lengths.add(len(name))

# Вывод обоих списков
print("Исходный список:", names)
print("Список uni:", uni)