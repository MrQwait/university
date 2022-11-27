s = input()

s1h = s[:s.find('h')]
s2h = s[s.rfind('h') + 1:]

s=s1h+s2h
print(s)