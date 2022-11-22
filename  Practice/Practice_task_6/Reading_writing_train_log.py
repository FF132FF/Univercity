import re


def read_log(requested_file):
    '''
    Функция принимает название файла; открывает и считывает этот файл; возвращает данные файла в виде текста
    :param requested_file: название файла (из которого мы возьмем данные)
    :return: данные из файла (в виде текста)
    '''
    content: TextIOWrapper = open(requested_file, encoding='utf-8')
    returned_file: str = content.read()
    return returned_file


def formatting_log(requested_file):
    '''
    Функция принимает название файла; применяет на него функцию read_log(); форматирует его в список; обрезает список
    для отображения нужных нам данных; возвращает обрезанный список
    :param requested_file: название файла (из которого мы возьмем данные)
    :return: отформатированные данные файла (в виде списка)
    '''
    content: str = read_log(requested_file)
    content: list = content.splitlines()
    del content[2::3]
    del content[1::2]
    return content


def save_log(returned_file, requested_file):
    '''
    Принимаем название файла; берем данные из этого файла; форматируем их в нужный нам вид; возвращаем отформатированные
    данные в нужный нам файл (returned_file)
    :param returned_file: Название файла (в который занесем отформатированные данные)
    :param requested_file: Название файла (из которого берем данные)
    :return: файл (с отформатированными данными)
    '''
    content: str = formatting_log(requested_file)
    content: str = ' '.join(content)
    timing: re.Pattern = re.compile(r'в (\d+:\d+:\d+)')
    timing_result: list = timing.findall(content)
    number: re.Pattern = re.compile(r'Рейс (\w+)')
    number_result: list = number.findall(content)
    place: re.Pattern = re.compile(r'\d\d\d \w+ (\w+ \w+)')
    place_result: list = place.findall(content)
    print(type(place_result))
    returned_file: TextIOWrapper = open(returned_file, mode='w+', encoding='utf-8')
    returned_file.write(str("# File content "))
    returned_file.write(str(returned_file.name))
    returned_file.write(str("\n\nTotal train log: \n"))
    count: int = 0

    while count != len(number_result):
        initial_log: list = ['[', timing_result[count], '] - Поезд № ', number_result[count], ' ', place_result[count]]
        final_log: str = ''.join(initial_log)
        returned_file.write(str(final_log))
        returned_file.write(str("\n"))
        count += 1

    return returned_file
