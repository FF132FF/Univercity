import re


def read_log(requested_file):
    '''

    :param requested_file:
    :return:
    '''
    content: TextIOWrapper = open(requested_file, encoding='utf-8')
    returned_file: str = content.read()
    return returned_file


def formatting_log(requested_file):
    '''

    :param requested_file:
    :return:
    '''
    content: str = read_log(requested_file)
    content: str = content.splitlines()
    del content[2::3]
    del content[1::2]
    return content


def save_log(returned_file, requested_file):
    '''

    :param returned_file:
    :param requested_file:
    :return:
    '''
    content: str = formatting_log(requested_file)
    content: str = ' '.join(content)
    timing: str = re.compile(r'в (\d+:\d+:\d+)')
    timing_result: str = timing.findall(content)
    number: str = re.compile(r'Рейс (\w+)')
    number_result: str = number.findall(content)
    place: str = re.compile(r'\d\d\d \w+ (\w+ \w+)')
    place_result: str = place.findall(content)
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
