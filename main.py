import string
import random


def pass_generator(length) :
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for ch in range(length))
    return password

length = int(input("Введите длинну пароля : "))

print('Ваш пароль: ', pass_generator(length))