a=input()
k=0
if a.count('f')==0:
    print(f'Букв f нет: {a.rfind("f")}')
elif a.count('f')==1:
    print(f'Позиция единственного вхождения буквы f: {a.index("f")}')
else:
    print(f'Первая и последняя позиция вхождения буквы f: {a.find("f")} и {a.rfind("f")}')