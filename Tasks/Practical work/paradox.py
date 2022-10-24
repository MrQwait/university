import random
def  monty_hall(k):
    count = 0
    count_changed_choice = 0

    for i in range(0, k):
        a = [0, 0, 1]
        player_choice = random.choice(a)
        if player_choice == 1:
            count += 1
        else:
            a.remove(0)
            a.remove(player_choice)
            if a[0] == 1:
                count_changed_choice += 1
    print(int(count_changed_choice / (count + count_changed_choice) * 100),'%',sep='')

def birthay(a):
    count=0
    k=[]
    day=[]
    month=[]

    for i in range (0, a):
        k.append(i+1)
        day.append(random.randint(1,28))
        month.append(random.randint(1,12))

    print(k,'\n',day,'\n', month, sep='')

    for i in range (0, len(k)-1):
        for d in range (i+1,len(k)):
            if day[i]==day[d] and month[i]==month[d]:
                count=count + 2
                print(k[i],day[i],month[i])
                print(k[d], day[d], month[d])
    print(int((count/a) * 100),'%',sep='')