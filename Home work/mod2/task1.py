# Найдите остаток при делении числа a на b.
# Формат ввода
# 123, 12
# Формат вывода
# 3
s = input().strip()
comma = s.find(',')
a = int(s[:comma].strip())
b = int(s[comma+1:].strip())
print(a % b)