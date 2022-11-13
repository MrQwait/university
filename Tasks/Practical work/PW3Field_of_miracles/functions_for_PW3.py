text = open('words.txt', encoding='utf-8')
w=text.readlines()
for i in range(len(w)):
    if '\n' in w[i]:
        w[i]=w[i].replace('\n','')

import random

def words():
    return random.choice(w)

def max_record(a):
    rec = open('record.txt')
    general_record = rec.read()
    rec.close()
    if int(general_record)>=a:
        print(f'Общий рекорд: {general_record}\n')
    if int(general_record)<a:
         print(f'Поздравляю! У вас новый рекорд')
         rec = open('record.txt', mode='w')
         rec.write(str(a))
         print(f'Общий рекорд:{a}\n')
         rec.close()
