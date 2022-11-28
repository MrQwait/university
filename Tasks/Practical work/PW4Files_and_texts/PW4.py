def read_file(t):
    '''
    Подсчитывает количество уникальных слов в текстовом файле.
    :param t: Файл
    :return: Список из уникальных слов (Не в алфавитном порядке)
    '''
    f = open(t, encoding='utf-8')
    text: list[str] = f.readlines()
    s: str = '()<>!;=-+*&?,.$[]{}'
    for i in range(len(text)):
        text[i] = text[i].replace(f'\n', '')
        for j in range(len(s)):
            if s[j] in text[i]:
                text[i] = text[i].replace(f'{s[j]}', '')
    #print(text)
    words: list[str] = []
    for i in range(len(text)):
        if text[i].count(' ') > 0:
            t_text = text[i].split(' ')
            for j in range(len(t_text)):
                words.append(t_text[j])
    for i in range(len(words)):
        words[i] = words[i].lower()
    words = set(words)
    words = list(words)
    f.close()
    print(words)
    return words


def save_file(text, words):
    '''
    Сортирует слова в алфивитном порядке и
    записывает их столбиком в файл. В 
    начале файла будет написано количество 
    уникальных слов.
    :param text: файл, в который мы записываем уникальные слова
    :param words: список уникальных слов
    :return:
    '''
    # alphabet='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    # sort_words=[]
    # for i in range(len(alphabet)):
    #     for j in range(len(words)):
    #         s=words[j]
    #         if alphabet[i]==s[0]:
    #             sort_words.append(s)
    sort_words = sorted(words)
    f = open(f'{text}', encoding='utf-8', mode='w')
    f.write(f'Кол-во уникальных слов: {len(sort_words)}\n')
    for i in range(len(sort_words)):
        f.write(sort_words[i] + '\n')
    f.close()


save_file('R_words.txt', read_file('data.txt'))
