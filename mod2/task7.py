# На вход подается строка s и символ i. Необходимо найти количество символов i, расположенных в начале строки.
# Формат ввода
# xyxxyx,x
# Формат вывода
# 1
s = input().strip()
comma = s.find(',')
text = s[:comma].strip()
ch = s[comma+1:].strip()
count = 0
for c in text:
    if c == ch:
        count += 1
    else:
        break
print(count)