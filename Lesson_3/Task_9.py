"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""


from random import random
m_row = 5
m_str = 5
my_list = []
for i in range(m_str):
    new_list = []
    for j in range(m_row):
        num = int(random() * 100)
        new_list.append(num)
    my_list.append(new_list)
for i in my_list:
    print(i)
m_max = -1
for j in range(m_row):
    m_min = 100
    for i in range(m_str):
        if my_list[i][j] < m_min:
            m_min = my_list[i][j]
    if m_min > m_max:
        m_max = m_min
print(f'Макс из мин: {m_max}')
