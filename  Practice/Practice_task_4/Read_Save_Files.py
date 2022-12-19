def read_file(requested_file: str):
    '''
    Функция принимает название файла; открывает и считывает этот файл; форматирует данные файла в список; возваращает
    этот список.
    :param requested_file: Название файла (из которого мы возьмем данные)
    :return: Список слов (находящихся в файле)
    '''
    content: TextIOWrapper = open(requested_file, "r+")
    returned_file: list = list(set(content.read().splitlines()))
    return returned_file


def save_file(returned_file: str, requested_file: str):
    '''
    Функция принимае название файла из которого мы возьмем данные и название файла в который запишем данные; сортирует
    полученный список; форматирует и записывает данные в файл, который и возвращает нам.
    :param returned_file: Название файла (в который мы запишем данные)
    :param requested_file: Название файла (из которого мы возьмем данные)
    :return: Файл (с записанным в него результатом)
    '''
    content: list = read_file(requested_file)
    content.sort()
    count: int = len(content)
    words: str = ' '.join(content)
    words: str = words.replace(" ", "\n")
    returned_file: TextIOWrapper = open(returned_file, mode='w+')
    returned_file.write(str("# File content "))
    returned_file.write(str(returned_file.name))
    returned_file.write(str("\nTotal unique words: "))
    returned_file.write(str(count))
    returned_file.write(str("\n===========\n"))
    returned_file.write(str(words))
    return returned_file
