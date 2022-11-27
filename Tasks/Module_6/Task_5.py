lst1 = [s for s in input().split()]
lst2 = [s for s in input().split()]
count = 0
for i in range(0, len(lst1)):
    for j in range(0, len(lst2)):
        if lst1[i] == (lst2[j]):
            count += 1
print(count)