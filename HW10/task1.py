# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv


from random import *


def generate_random_name():
    while True:
        letters = 'abcdefghijklmnopqrstuvwxyz'
        text1 = ''.join(choice(letters) for letter in range(randint(1, 15)))
        text2 = ''.join(choice(letters) for letter in range(randint(1, 15)))
        yield f'{text1} {text2}'


gen = generate_random_name()
print(next(gen))

