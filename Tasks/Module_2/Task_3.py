a=int(input('Введите число больше 9 '))
print(f'Последние 2 цифры числа {a}:', (a % 100) // 10, a % 10)