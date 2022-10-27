#PW2 Birthay
import random
def birthay(a,b):
    count=0
    for i in range (0, a):
        day=[]
        for j in range (0,b):
            d=random.randint(1,365)
            if d in day:
                count=count+1
                break
            else:
                day.append(d)
    print((count/a)*100,'%',sep='')


if __name__=='__main__':
    a=int(input())
    b=int(input())
    birthay(a,b)