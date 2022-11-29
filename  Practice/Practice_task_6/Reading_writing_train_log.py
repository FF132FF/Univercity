import re


def read_log(requested_file: str):
    '''
    Функция принимает название файла; открывает и считывает этот файл; возвращает данные файла в виде текста.
    :param requested_file: Название файла (из которого мы возьмем данные)
    :return: Данные из файла (в виде текста)
    '''
    content: TextIOWrapper = open(requested_file, encoding='utf-8')
    returned_file: str = content.read()
    return returned_file


def formatting_and_save_log(requested_file: str, returned_file: str):
    '''
    Функция принимает название файла данные которого будем считывать и форматировать, а затем название файла, который
    мы будем использовать для хранения отформатированных данных; применяет на первый файл функцию read_log();
    форматирует его в нужный нам вид; записывает данные во второй заданный файл; возвращает сообщение об успешном
    окончании работы.
    :param requested_file: Название файла (из которого мы возьмем данные)
    :param returned_file: Название файла (в который мы запишем данные)
    :return: Сообщение об окончании работы
    '''
    content: str = read_log(requested_file)
    content: list = content.splitlines()
    pattern: str = r"(?:^Рейс) (\d+) (?:прибыл|отправился) (\w+) (\w+) (?:\w+) (\d+:\d+:\d+)"
    changed_log: TextIOWrapper = open(returned_file, mode='w+', encoding='utf-8')
    changed_log.write(str("# File content "))
    changed_log.write(str(changed_log.name))
    changed_log.write(str("\n\nTotal train log: \n"))
    for element in content:
        content: re.Pattern = re.findall(pattern, element)
        if len(content) == 1:
            result_list: tuple = content[0]
            initial_log: list = ['[', result_list[3], '] - Поезд № ', result_list[0], ' ', result_list[1], ' ',
                                 result_list[2]]
            final_log: str = ''.join(initial_log)
            changed_log.write(str(final_log))
            changed_log.write(str("\n"))
        else:
            continue
    return "\n===Данные отформатированы и сохранены в указанный файл===\n"
