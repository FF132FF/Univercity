import csv
import re


def converter():
    '''
    Преобразовывает books.csv в books_converted.txt (не уверен что это требуется, но сделано, т.к. легче понимается);
    Возвращаем название файла (с преобразованными данными из csv в txt)
    :return: Название файла (с преобразованными данными из csv в txt)
    '''
    with open("books.csv", 'r', encoding='utf-8') as f:
        books: _csv.reader = csv.reader(f, delimiter=',')
        converted_file: TextIOWrapper = open("books_converted.txt", mode='w+', encoding='utf-8')
        for row in books:
            book_elements: str = ''.join(row)
            converted_file.write(str(book_elements))
            converted_file.write(str("\n"))
    return "books_converted.txt"


def creating_a_list_of_books_elements():
    '''
    Создаем общий список списоков параметров книг; возвращаем этот список
    :return: Список (созданный нами общий список списков параметров книг)
    '''
    books_pattern: str = r"(?P<isbn>\d+\-\d\-\d+\-\d+\-\d)(?:\|+)(?P<title>[^\|]*)(?:\|+)(?P<author>[^\|]*)(?:\|+)" \
                         r"(?P<quantity>[^\|]*)(?:\|+)(?P<price>[^\n]*)"
    converted_file: TextIOWrapper = open("books_converted.txt", mode='r+', encoding='utf-8')
    content: str = converted_file.read()
    list_of_books: list = re.findall(books_pattern, content)
    return list_of_books


def get_books(keyword: str):
    '''
    Получаем на вход ключевое слово; производим поиск совпадений в списках из функции creating_a_list_of_books_elements
    по этому ключевому слову; возвращаем список списков, в которых найдены совпадения с ключевым словом
    :param keyword: Ключевое слово
    :return: Список (список списков, в которых найдены совпадения с ключевым словом)
    '''
    list_of_books: list = creating_a_list_of_books_elements()
    with_matches: list = []
    for element in list_of_books:
        for book_element in element:
            book_element_str: str = ''.join(book_element)
            book_element_str_lower: str = book_element_str.lower()
            if keyword in book_element_str_lower:
                with_matches.append(element)
    return with_matches


def get_totals(list_of_books):
    '''
    Принимаем список списков из функции creating_a_list_of_books_elements(); приводим к виду [(isbn, quantity * price)];
    возвращаем отформатированный список
    :param list_of_books: Список списков (из функции creating_a_list_of_books_elements())
    :return: Список (отформатированный список вида [(isbn, quantity * price)])
    '''
    books_elements: list = list_of_books
    books_totals: list = []
    for book_elements in books_elements:
        quantity_multiply_price: float = int(book_elements[3]) * float(book_elements[4])
        if quantity_multiply_price < 500:
            quantity_multiply_price += 100
        books_totals.append((book_elements[0], quantity_multiply_price))
    return books_totals
