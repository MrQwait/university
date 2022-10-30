n=[]
while True:
    a=int(input())
    n.append(a)
    if a==0:
        break

count=0
i=0
while i < len(n)-1:
    if n[i] < n[i + 1]:
        count = count + 1
    i += 1
print(count)


