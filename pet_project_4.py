import random

x = int(input('Введите длину пароля:'))
f = ''

for i in range(x + 1):
    f += random.choice(list('1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

print(f)
