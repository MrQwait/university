import csv


def get_books(substring: str) -> list:
    books: list = []
    with open('books.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='|')
        for row in reader:
            if substring.lower() in row[1].lower():
                books.append(row)
    return books


def get_totals(books: list) -> list:
    result: list = []
    for book in books:
        price: float = float(book[3]) * float(book[4])
        if price >= 500:
            result.append((book[0], price))
        else:
            result.append((book[0], price + 100))
    return result


print(get_books('python'))
print(get_totals(get_books('python')))
