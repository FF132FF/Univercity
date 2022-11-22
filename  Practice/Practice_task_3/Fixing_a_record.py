def get_word():
    '''
    Функция открывает и  считывает файл, который является словарем игры; Записывает слова, разделяя их в список
    по одному слову; этот список является словарем игры; Возвращает словарь игры в виде списка.
    :return: Возвращает список слов
    '''
    words: TextIOWrapper = open('Dictionary.txt')
    Dictionary: list = words.read().split()
    Dictionary = [i.lower() for i in Dictionary]
    return Dictionary


def fixing_a_record(current_Record):
    '''
    Функция принимает текущий рекорд игрока; открывает файл максимальным рекордом; считывает этот рекорд; сравнивает
    текущий рекорд игрока с максимальным рекордом; Если текущий рекорд игрока лучше максимального, заменяет максималный
    рекорда на новый; Возвращает разделитель (весь вывод отображается внутри функции, поэтому такой return)
    :param current_Record: Текущий рекорд
    :return: Возвращает разделитель
    '''
    record_in_file: TextIOWrapper = open("Record.txt", mode='r+')
    max_record: int = int(record_in_file.read())
    if current_Record > max_record:
        max_record: int = current_Record
    record_in_file.seek(0)
    record_in_file.write(str(max_record))
    print("      Current record:", current_Record, "=== Max record:", max_record)
    separator: str = "=============================================="
    return separator
