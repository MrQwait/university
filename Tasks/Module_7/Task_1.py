text=input().split(' ')
answer='0 '
for i in range(len(text)):
    count=0
    for j in range(0, i):
        if text[i]==text[j]:
            count=count+1
        if j==(i-1):
            answer=answer+f'{count} '
print(answer)