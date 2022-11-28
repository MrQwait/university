import random


def monty_hall(count_plays: int) -> str:
    '''
    Парадокс Монти Холла
    :param count_plays: число (Количество игр)
    :return: процент побед
    '''
    count: int = 0
    count_changed_choice: int = 0

    for i in range(0, count_plays):
        a: list[int] = [0, 0, 1]
        player_choice = random.choice(a)
        if player_choice == 1:
            count += 1
        else:
            a.remove(0)
            a.remove(player_choice)
            if a[0] == 1:
                count_changed_choice += 1
    return (str(int(count_changed_choice / (count + count_changed_choice) * 100)) + '%')


print(monty_hall(int(input())))
