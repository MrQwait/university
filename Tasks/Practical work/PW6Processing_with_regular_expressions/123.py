import re

pattern=r'Рейс (\d+) (?:прибыл|отправился) (из|в) (\w+) в (\d+:\d+:\d+)'

with open("Travel_Journal.txt", "r", encoding="utf-8") as text:
    text=text.read()
    response=re.findall(pattern, text)

with open("new_travel_journal.txt", "w", encoding="utf-8") as add_text:
    for num in response:
        add_text.write(f'[{num[3]}]: - Поезд № {num[0]} {num[1]} {num[2]}\n')