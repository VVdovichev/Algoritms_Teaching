"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""


from random import random
N = 10
my_list = [0] * N
for i in range(N):
    my_list[i] = int(random() * 50)
print(my_list)

min_id = 0
max_id = 0
for i in range(1, N):
    if my_list[i] < my_list[min_id]:
        min_id = i
    elif my_list[i] > my_list[max_id]:
        max_id = i
print(my_list[min_id], my_list[max_id])

if min_id > max_id:
    min_id, max_id = max_id, min_id

summa = 0
for i in range(min_id+1, max_id):
    summa += my_list[i]
print(summa)
