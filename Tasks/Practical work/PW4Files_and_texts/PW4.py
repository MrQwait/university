def read_file(t):
    f=open(f'{t}', encoding='utf-8')
    text=f.readlines()
    for i in range(len(text)):
        text[i]=text[i].replace('\n','')
        text[i]=text[i].replace('.','')
        text[i]=text[i].replace(',', '')
        text[i] = text[i].replace('!', '')
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
    for i in range(len(sort_words)):
        f.write(sort_words[i]+'\n')
    f.close()


save_file('R_words.txt',read_file('data.txt'))
