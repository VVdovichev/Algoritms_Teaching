"""
Написать программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
1+2+...+n = n(n+1)/2, где n — любое натуральное число.
"""


n = int(input('Введите натуральное число: '))


def first(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s


def second(n):
    return n * (n + 1) // 2


if first(n) == second(n):
    print(f'Для n = {n} - True')
else:
    print(f'Для n = {n} - False')

print(first(n))
print(second(n))
