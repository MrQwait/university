lst = [s for s in input().split()]
sort_lst = []
for i in range(0, len(lst) - 1, 2):
        sort_lst.append(lst[i + 1])
        sort_lst.append(lst[i])
if len(lst) % 2 != 0:
    sort_lst.append(lst[len(lst) - 1])
print(" ".join(sort_lst))