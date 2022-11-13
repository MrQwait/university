from functions_for_PW3 import *
def game():
    while True:
        answer=input('Выберите уровень сложности\n1 - Легкий  (7 жизней)\n2 - Средний (5 жизней)\n3 - Сложный (3 жизни)\n')
        if answer == '1':
            life = 7
            break
        if answer == '2':
            life = 5
            break
        if answer == '3':
            life = 3
            break
    selected_word=words()
    #print(selected_word)

    hidden_word=[]
    for i in range(len(selected_word)):
        hidden_word.append('\u25A0 ')

    while life>0:
        str_hidden_word = ''
        for i in range(len(hidden_word)):
            str_hidden_word=str_hidden_word+hidden_word[i]
        if str_hidden_word==selected_word:
            break

        player_choice=input(f'{str_hidden_word}|♥{life}\nНазовите букву или слово целиком: ')

        if player_choice == selected_word:
            break
        elif player_choice in selected_word:
            for i in range(len(selected_word)):
                if selected_word[i] == player_choice:
                    hidden_word[i]=player_choice
        else:
            print('Такой буквы в этом слове нет. Вы теряете жизнь')
            life=life-1
    if life==0:
        print(f'Вы програли\nЗагаданное слово:{selected_word}')
        return 0
    else:
        print('Вы выйграли! Приз в студию!')
        return 1
c_win=0
ws=''
while True:
    answer=input(f'Хотите сыграть в игру {ws} ?\nНапишите "да" или "нет"\n')
    if answer == 'да':
        ws='ещё раз'
        if game()==1:
            c_win=c_win+1
            print(f'Ваш текущий рекорд: {c_win}')
            max_record(c_win)
        else:
            c_win=0
            print('Сброс текущего рекорда\n')
    if answer == 'нет':
        print('Хорошего дня!')
        text.close()
        break
