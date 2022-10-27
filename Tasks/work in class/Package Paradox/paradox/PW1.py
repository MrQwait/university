#PW1 Monty hall
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


if __name__=='__main__':
    k=int(input())
    monty_hall(k)