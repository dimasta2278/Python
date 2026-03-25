# 2. Email'ы могут состоять из любых букв латинского алфавита верхнего и нижнего регистров, цифр, спецсимволов из набора “+_- #”.
# Выведите email'ы в столбец.

# Sample Input:
# Jones and Palin met at Oxford University, where they performed together ysinghmanga@206954.com with the Oxford Revue. (6boutheina+14@weammo.xyz)


import re

text = input("Введите текст: ")

# Дефис в конце символьного класса, чтобы он не интерпретировался как диапазон
pattern = r'[a-zA-Z0-9+_#-]+@[a-zA-Z0-9.-]+'

emails = re.findall(pattern, text)

for email in emails:
    print(email)
    