print('Введите три целых числа, программа выведет кол-во одинаковых чисел ')
a=int(input())
b=int(input())
c=int(input())
if a!=b and a!=c and b!=c:
    print('0')
elif (a==b and a!=c) or (a==c and a!=b) or (b==c and b!=a):
    print('2')
else:
    print('3')