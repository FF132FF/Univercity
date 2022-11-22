import re

def read_log(requested_file):
    content = open(requested_file, encoding='utf-8')
    returned_file = content.read()
    return returned_file

def formatting_log(requested_file):
    content = read_log(requested_file)
    content = content.splitlines()
    del content[2::3]
    del content[1::2]
    return content

def save_log(returned_file, requested_file):
    content = formatting_log(requested_file)
    content = ' '.join(content)
    timing = re.compile(r'в (\d+:\d+:\d+)')
    timing_result = timing.findall(content)
    number = re.compile(r'Рейс (\w+)')
    number_result = number.findall(content)
    place = re.compile(r'\d\d\d \w+ (\w+ \w+)')
    place_result = place.findall(content)
    returned_file = open(returned_file, mode='w+', encoding='utf-8')
    returned_file.write(str("# File content "))
    returned_file.write(str(returned_file.name))
    returned_file.write(str("\n\nTotal train log: \n"))
    count = 0
    while count != len(number_result):
        initial_log = ['[', timing_result[count], '] - Поезд № ', number_result[count], ' ', place_result[count]]
        final_log = ''.join(initial_log)
        returned_file.write(str(final_log))
        returned_file.write(str("\n"))
        count += 1

    return returned_file

