print('Введите четыре целых числа от 1 до 8 (Координаты шахматной доски), программа выведет ДА если одинаковый цвет у двух пар координат, иначе выведет НЕТ')
a=int(input())
b=int(input())
#Если переменная a - чётная,то она = 1 и она на белой клетке, иначе на чёрной и = 0
#Если переменная b - чётная,то она = 0 и она на чёрной клетке, иначе на белой и = 1
a2=int(input())
b2=int(input())
if a % 2==0:
    a=1
else:
    a=0

if b % 2==0:
    b=0
else:
    b=1

if a==b:
    k=1
    print('Белая')
else:
    k=0
    print('Чёрная')

if a2 % 2==0:
    a2=1
else:
    a2=0
if b2 % 2==0:
    b2=0
else:
    b2=1
if a2 == b2:
    k2 = 1
    print('Белая')
else:
    k2 = 0
    print('Чёрная')
if k==k2:
    print('Да')
else:
    print('Нет')