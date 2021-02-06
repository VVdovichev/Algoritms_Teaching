"""
В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то,
что загадано. Если за 10 попыток число не отгадано, вывести ответ.
"""


from random import random
n = round(random() * 100)
i = 1
print("Компьютер загадал число. Отгадайте его. У вас 10 попыток")
while i <= 10:
    u = int(input(str(i) + '-я попытка: '))
    if u > n:
        print('Много')
    elif u < n:
        print('Мало')
    else:
        print(f'Вы угадали с {i}-й попытки')
        break
    i += 1
else:
    print('Вы исчерпали 10 попыток. Было загадано: ', n)
