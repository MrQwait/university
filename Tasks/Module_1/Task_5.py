a=int(input('Кол-во студентов '))
b=int(input('Кол-во яблок '))
print(f'Яблок на студента: {b // a}')
print(f'Яблок осталось: {b-(b // a)*a}')