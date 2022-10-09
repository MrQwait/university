tk={}
NameK=[]
def NameCorrector(name):
    name.lower()
    brokenName=name.split(' ')
    brokenName[0]=brokenName[0].capitalize()
    brokenName[1]=brokenName[1].capitalize()
    name=brokenName[0]+' '+brokenName[1]
    return name
def NumberCorrector(nt):
    nt = nt.replace(' ', '').replace('-', '')
    if nt[:2] == '+7' and len(nt) == 12:
        return nt
    if nt[0] == '9' and len(nt) == 10:
        nt = '+7' + nt
        return nt
    if nt[0] == '8' and len(nt) == 11:
        nt = nt.replace('8', '+7', 1)
        return nt
    else:
        print('Неверно введен номер телефона')
        return 0
def NPN(a):
    if a == 1:
        print('Введите имя и фамилию контакта')
        name=input()
        print('Введите номер телефона контакта ')
        nt=input()
        if NumberCorrector(nt)!=0:
            NameK.append(NameCorrector(name))
            tk[NameCorrector(name)]=NumberCorrector(nt)
    if a == 2:
        print('Введите имя контакта, которое хотите удалить')
        name=input()
        name=NameCorrector(name)
        if name in tk:
            tk.pop(name)
            print('Контакт удален')
        else:
            print('Такого контакта нет')
    if a == 4:
        print('Введите имя и фамилию контакта, телефон которого вы хотите изменить')
        name = input()
        name = NameCorrector(name)
        if name in tk:
            print('Введите новый номер телефона')
            nt=input()
            nt=NumberCorrector(nt)
            if nt!=0:
                tk[name]=nt
                print('Телефон контакта изменён')
        else:
            print('Такого контакта нет')

while True:
    print('')
    print('1 - Добавить контакт')
    print('2 - Удалить контакт')
    print('3 - Просмотреть телефонную книгу')
    print('4 - Изменить номер телефона по имени')
    print('5 - закончить программу')
    a=int(input())
    if a==1:
        NPN(a)
    if a==2:
        NPN(a)
    if a==3:
        for i in range (len(NameK)):
            if NameK[i] in tk:
                print(NameK[i],tk[NameK[i]])
    if a==4:
        NPN(a)
    if a==5:
        break

