"""
 Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
 Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
 В конце следует вывести полученную матрицу.
"""


m_row = 5
m_str = 4
my_list = []
for i in range(m_str):
    new_list = []
    summa = 0
    print(f'{i + 1} строка')
    for j in range(m_row - 1):
        num = int(input(f'Введите число: '))
        summa += num
        new_list.append(num)
    new_list.append(summa)
    my_list.append(new_list)
for i in my_list:
    print(i)
