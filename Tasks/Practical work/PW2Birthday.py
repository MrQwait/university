import random


def birthay(count_students: int) -> str:
    '''
    Парадокс дней рождения
    :param count_students: число (количество учащихся)
    :return: процент совпадения дней рождений
    '''
    count: int = 0
    students: list[int] = []
    day: list[int] = []
    month: list[int] = []

    for i in range(0, count_students):
        students.append(i + 1)
        day.append(random.randint(1, 28))
        month.append(random.randint(1, 12))

    print(students, '\n', day, '\n', month, sep='')

    for i in range(0, len(students) - 1):
        for d in range(i + 1, len(students)):
            if day[i] == day[d] and month[i] == month[d]:
                count = count + 2
                print(students[i], day[i], month[i])
                print(students[d], day[d], month[d])
    return (str(int((count / a) * 100)) + '%')


a = int(input())
print(birthay(a))
