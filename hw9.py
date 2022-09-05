# ДЗ 9:
# Напишите функцию, которая будет генерировать случайный пароль. В пароле должно быть от 7 до 10 символов,
# при этом каждый символ должен быть случайным образом выбран из диапазона от 33 до 126 в таблице
# ASCII. Ваша функция не должна принимать на вход параметры, а возвращать будет сгенерированный пароль.
# В основной программе вы должны просто вывести созданный случайным образом пароль. Программа должна запускаться
# только в том случае, если она не импортирована в виде
# модуля в другой файл.
import sys
import random


def random_password():
    pw = []
    x = random.randint(7, 11)
    for y in range(x):
        d = random.randint(33, 127)
        pw.append(chr(d))

    return ''.join(pw)


modulename = 'hw9'

if modulename not in sys.modules:
    res = random_password()
    print(res)
else:
    print("Your program imported as a module")
