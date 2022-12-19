def get_word():
    '''
    Функция открывает и  считывает файл, который является словарем игры; Записывает слова, разделяя их в список
    по одному слову; этот список является словарем игры; Возвращает словарь игры в виде списка.
    :return: Список слов
    '''
    words: TextIOWrapper = open('Dictionary.txt')
    dictionary: list = words.read().split()
    dictionary = [i.lower() for i in dictionary]
    print(type(dictionary))
    return dictionary


def fixing_a_record(current_record):
    '''
    Функция принимает текущий рекорд игрока; открывает файл максимальным рекордом; считывает этот рекорд; сравнивает
    текущий рекорд игрока с максимальным рекордом; Если текущий рекорд игрока лучше максимального, заменяет максималный
    рекорда на новый; Возвращает разделитель (весь вывод отображается внутри функции, поэтому возвращает его)
    :param current_record: Текущий рекорд
    :return: Разделитель
    '''
    record_in_file: TextIOWrapper = open("Record.txt", mode='r+')
    max_record: int = int(record_in_file.read())
    if current_record > max_record:
        max_record: int = current_record
    record_in_file.seek(0)
    record_in_file.write(str(max_record))
    print("      Current record:", current_record, "=== Max record:", max_record)
    separator: str = "=============================================="
    return separator
