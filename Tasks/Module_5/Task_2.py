X = int(input('Введите целое число '))
N = 0

while 2 ** (N + 1) <= X:
    N = N + 1

print(N, 2 ** N)