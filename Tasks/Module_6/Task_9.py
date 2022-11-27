s = input()
ls = s[len(s) // 2 + len(s) % 2:]
rs = s[: len(s) // 2 + len(s) % 2]
print(ls + rs)