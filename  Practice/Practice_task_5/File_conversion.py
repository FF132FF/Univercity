def read_file(requested_file: str):
    '''
    :param requested_file: Получает название, пытается найти его и прочитать
    :return: Eсли такой файл есть, возвращает его. Если нету, возвращает специальный файл, который означает ошибку
    '''
    try:
        content: TextIOWrapper = open(requested_file, "r+")
    except:
        requested_file = "ErrorFileNotFound.txt"
        return requested_file
    content: TextIOWrapper = open(requested_file, "r+")
    returned_file = content.read().splitlines()
    return returned_file


def file_conversion(requested_file: str):
    '''
    :param requested_file: Получает название, пытается найти его и прочитать, затем преобразовывает в нужный формат
    :return: Eсли файл соотвествует требованиям, возвращает преобразованный файл. Если количество чисел в файле не соответствует первому значению, возвращает ошибку
    '''
    returned_file = read_file(requested_file)
    print(type(returned_file))
    returned_file = list(map(int, returned_file))
    save: int = returned_file[0]
    del returned_file[0]
    if save == len(returned_file):
        return returned_file
    else:
        broken: str = "Количество чисел не соответствует первому значению!"
        return