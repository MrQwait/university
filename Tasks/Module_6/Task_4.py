lst = [s for s in input().split()]
max_num = -100000
min_num = 100000
max_index = 0
min_index = 0

for i in range(0, len(lst)):
    if int(lst[i]) > int(max_num):
        max_num = lst[i]
        max_index = i
    if int(lst[i]) < int(min_num):
        min_num = lst[i]
        min_index = i

lst[max_index] = min_num
lst[min_index] = max_num

print(" ".join(lst))