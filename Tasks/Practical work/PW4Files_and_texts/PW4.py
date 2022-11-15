def read_file(t):
    f=open(f'{t}', encoding='utf-8')
    text=f.readlines()
    s='()<>!;=-+*&?,.$[]{}'
    for i in range(len(text)):
        text[i] = text[i].replace(f'\n', '')
        for j in range(len(s)):
            if s[j] in text[i]:
                text[i]=text[i].replace(f'{s[j]}','')
    words=[]
    for i in range(len(text)):
        if text[i].count(' ')>0:
            t_text=text[i].split(' ')
            for j in range(len(t_text)):
                words.append(t_text[j])
    for i in range(len(words)):
        words[i]=words[i].lower()
    words=set(words)
    words=list(words)
    f.close()
    return words

def save_file(text, words):
    alphabet='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    sort_words=[]
    for i in range(len(alphabet)):
        for j in range(len(words)):
            s=words[j]
            if alphabet[i]==s[0]:
                sort_words.append(s)
    f = open(f'{text}', encoding='utf-8',mode='w')
    f.write(f'Кол-во уникальных слов: {len(sort_words)}\n')
    for i in range(len(sort_words)):
        f.write(sort_words[i]+'\n')
    f.close()


save_file('R_words.txt',read_file('data.txt'))
