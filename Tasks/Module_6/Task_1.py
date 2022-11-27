list = [s for s in input().split()]
sort_list = []

for i in list:
    if int(i) % 2 != 0:
        sort_list.append(i)

print(" ".join(sort_list))