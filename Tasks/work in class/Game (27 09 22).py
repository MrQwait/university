import random
k=0
r=0
max=0
f=0
while True:
    if f==1:
        print(' ')
        print('Поиграем ещё раз ?')
        print('1 - Да')
        print('2 - Нет')
        e=input()
        if e!='2' and e!='1':
            print('Некорректный ввод')
            continue
        else:
            if int(e)==2:
                break
            else:
                f=0
    k=k+1
    a=random.randint(1,100)
    b=random.randint(1,100)
    sab=a+b
    i=int(input(f'Пример {k}: {a} + {b} = '))
    if i==sab:
        r=r+1
        print(f'Верно! Кол-во баллов: {r}')
    else:
        if r>max:
            max=r
        print('Ты ошибся! Сброс баллов')
        print(f'Твой рекорд: {max}')
        r=0
        f=1
print('Хорошего дня!')
