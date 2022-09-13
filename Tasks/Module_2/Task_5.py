a=int(input('Введите число из 3 цифр '))
b=a
s=0
while a>0:
    x=a % 10
    s=x+s
    a=a // 10
print(f'сумма цифр числа {b} =',s)