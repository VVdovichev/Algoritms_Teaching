"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""


from random import random
n = 10
my_list = [0] * n
new_list = []
for i in range(n):
    my_list[i] = int((random() * 10) - 20)
print(my_list)
i = 0
index = -1
while i < n:
    if my_list[i] < 0 and index == -1:
        index = i
    elif my_list[index] < my_list[i] < 0:
        index = i
    i += 1
print(f'my_list[{index}]: {my_list[index]}')