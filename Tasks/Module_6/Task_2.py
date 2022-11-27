lst = [s for s in input().split()]
sort_lst = []
for i in range(0, len(lst) - 1):
    if int(lst[i]) < int(lst[i + 1]):
        sort_lst.append(lst[i + 1])

print(" ".join(sort_lst))