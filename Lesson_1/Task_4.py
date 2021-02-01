start = ord(input('1-я буква: '))
stop = ord(input('2-я буква: '))
start = start - ord('a') + 1
stop = stop - ord('a') + 1
print(f'\tПозиции: {start} и {stop}')
print('\tМежду буквами символов:', abs(start - stop) - 1)
