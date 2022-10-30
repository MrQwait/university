a=int(input())
p=[0,1]
i=0
np=0
while True:
    np=p[i]+p[i+1]
    p.append(np)
    i=i+1
    if a==np:
        print(i+1)
        break
    if a<np:
        print('-1')
        break