"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""


from random import random
n = 10
my_list = [0] * n
for i in range(n):
    my_list[i] = int(random() * 100)
    print(my_list[i], end=' ')
min_num = 0
max_num = 0
for i in range(n):
    if my_list[i] < my_list[min_num]:
        min_num = i
    elif my_list[i] > my_list[max_num]:
        max_num = i
print()
print(f'my_list[{min_num}] = {my_list[min_num]}\nmy_list[{max_num}] = {my_list[max_num]} ')
x = my_list[min_num]
my_list[min_num] = my_list[max_num]
my_list[max_num] = x
for i in range(10):
    print(my_list[i], end=' ')

