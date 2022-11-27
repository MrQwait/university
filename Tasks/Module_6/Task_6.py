lst1 = [s for s in input().split()]
lst2 = [s for s in input().split()]
sort_list=[]
for i in range(0, len(lst1)):
    for j in range(0, len(lst2)):
        if lst1[i] == (lst2[j]):
            sort_list.append(lst1[i])
print(' '.join(sort_list))