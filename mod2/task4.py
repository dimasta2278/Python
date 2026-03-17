# Для введенного в десятичном коде натурального числа найти представление в двоичном, восьмеричном и шестнадцатеричном кодах. Если введено не натуральное число, вывести диагностику: «Неверный ввод». Использовать встроенные возможности языка python запрещено.
# Формат ввода
# 100
# Формат вывода
# 1100100, 144, 64
# Коды
s = input().strip()
# Проверка на натуральное число
if not s.isdigit() or int(s) <= 0:
    print("Неверный ввод")
else:
    num = int(s)
    # Двоичная
    def to_base(n, base):
        digits = "0123456789ABCDEF"
        res = ""
        while n > 0:
            res = digits[n % base] + res
            n //= base
        return res
    bin_str = to_base(num, 2)
    oct_str = to_base(num, 8)
    hex_str = to_base(num, 16)
    print(f"{bin_str}, {oct_str}, {hex_str}")