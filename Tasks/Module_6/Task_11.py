s = input()

word = s[:s.find('h')]
word += s[s.find('h')+1:s.rfind('h')+1][::-1]
word += s[s.rfind('h'):]

print(word)