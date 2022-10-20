N = int(input())
h = N // 60
m = N % 60
if m < 10:
    print(f'{hour}:0{m}')
else:
    print(f'{hour}:{m}')