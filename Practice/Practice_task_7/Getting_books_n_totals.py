import csv


def get_list():
    '''
    Открывает и считывает данный csv файл; преобразовывает его в список; взвращает этот список
    :return: Список (список списков сток, взятых из csv файла)
    '''
    with open("books.csv", 'r', encoding='utf-8') as f:
        books: _csv.reader = csv.reader(f, delimiter=',')
        books = list(books)
        list_of_books = []
        for row in books:
            row = ''.join(row)
            row = row.split("|")
            list_of_books.append(row)
        list_of_books.remove(list_of_books[0])
    return list_of_books


def get_books(keyword: str):
    '''
    Получаем на вход ключевое слово; производим поиск совпадений в списках из функции get_list() по этому ключевому
    слову; возвращаем список списков, в которых найдены совпадения с ключевым словом
    :param keyword: Ключевое слово
    :return: Список (список списков, в которых найдены совпадения с ключевым словом)
    '''
    list_of_books: list = get_list()
    with_matches: list = []
    for element in list_of_books:
        for book_element in element:
            book_element_str: str = ''.join(book_element)
            book_element_str_lower: str = book_element_str.lower()
            keyword: str = keyword.lower()
            if keyword in book_element_str_lower:
                with_matches.append(element)
    return with_matches


def get_totals(list_of_books: list):
    '''
    Принимаем список списков из функции get_list; приводим к виду [(isbn, quantity * price)];
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
