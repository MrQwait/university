num = [int(s) for s in input().split()]
num2 = []
for num in num:
    if num in num2:
        print("ДА")
    else:
        print("НЕT")
        num2.append(num)