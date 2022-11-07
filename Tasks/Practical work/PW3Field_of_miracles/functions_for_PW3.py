text = open('words.txt', encoding='utf-8')
w=text.readlines()
for i in range(len(w)):
    if '\n' in w[i]:
        w[i]=w[i].replace('\n','')

import random

def words():
    return random.choice(w)
#def max_record(a):
    #with open('record.txt', 'a') as f:
        #f.write(a)