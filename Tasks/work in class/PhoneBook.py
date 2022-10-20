tk={}
NameK=[]
def NameCorrector():
    name = input('Введите имя и фамилию контакта \n')
    name.lower()
    name_surname = name.split(' ')
    for i in range(0, len(name_surname)):
        name_surname[i] = name_surname[i].capitalize()
    name = ' '.join(name_surname)
    return name

def NumberCorrector():
    nt = input('Введите номер телефона контакта \n')
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
        return NumberCorrector()

def addContact(nameAdd,ntAdd):
        NameK.append(nameAdd)
        tk[nameAdd]=ntAdd
        print('Контакт добавлен')

def delcontact(delname):
        if delname in tk:
            tk.pop(delname)
            print('Контакт удален')
        else:
            print('Такого контакта нет')

def changeContact(CCname):
        if CCname in tk:
            tk[CCname]=NumberCorrector()
            print('Телефон контакта изменён')
        else:
            print('Такого контакта нет')

while True:
    print('\n 1 - Добавить контакт \n 2 - Удалить контакт \n 3 - Просмотреть телефонную книгу \n 4 - Изменить номер телефона по имени \n 5 - закончить программу')
    a=int(input())
    if a==1:
        addContact(NameCorrector(),NumberCorrector())
    if a==2:
        delcontact(NameCorrector())
    if a==3:
        for i in range (len(NameK)):
            if NameK[i] in tk:
                print(NameK[i],tk[NameK[i]])
    if a==4:
        changeContact(NameCorrector())
    if a==5:
        break