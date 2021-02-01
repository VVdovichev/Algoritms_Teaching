print('Введите три числа')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if b < a < c or b > a > c:
    print(f'Среднее число а = {a}')
elif a < b < c or a > b > c:
    print(f'Среднее число b = {b}')
elif a < c < b or a > c > b:
    print(f'Среднее число с = {c}')
else:
    print('Все числа равны')
