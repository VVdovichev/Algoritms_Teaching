"""
Определить, какое число в массиве встречается чаще всего.
"""


from random import random
n = 30
my_list = [0] * n
new_list = []
for i in range(n):
    my_list[i] = int(random() * 100)
print(my_list)
print()
num = my_list[0]
max_quantity = 1
for i in range(n - 1):
    quantity = 1
    for x in range(i + 1, n):
        if my_list[i] == my_list[x]:
            quantity += 1
    if quantity > max_quantity:
        max_quantity = quantity
        num = my_list[i]
if max_quantity > 1:
    print(f'{max_quantity} раз(а) встречается число {num}')
else:
    print('Все числа уникальны!')
