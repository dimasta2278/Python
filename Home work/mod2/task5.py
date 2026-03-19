# На вход подается доменное имя сайта. Необходимо вывести все домены по порядку начиная с домена первого уровня.
# Формат ввода
# www.google.com
# Формат вывода
# com
# google
# www
# Домены
domain = input().strip()
while True:
    dot = domain.rfind('.')
    if dot == -1:
        print(domain)
        break
    else:
        print(domain[dot+1:])
        domain = domain[:dot]