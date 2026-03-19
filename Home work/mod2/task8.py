# Дан список слов. Составить из последних букв каждого слова новое.
# Формат ввода
# кот гири док
# Формат вывода
# тик
# Последние символы
s = input().strip()
result = ""
word = ""
for ch in s:
    if ch == ' ':
        if word:  # если слово не пустое
            result += word[-1]
            word = ""
    else:
        word += ch
# последнее слово
if word:
    result += word[-1]
print(result)