def read_file(requested_file: str):
    '''
    Принимает название файла и пытается открыть этот файл; если файл не открывается и выдает ошибку, то название
    запрошенного файла изменяется на "ErrorFileNotFound.txt" и возвращает его как ошибку; если файл открывается и не
    выдает ошибку, считывает файл и записывает числа из файла в список и возвращает этот список
    :param requested_file: Название файла
    :return: Eсли такой файл есть, возвращает список чисел в нем; если нет, возвращает специальный файл, который
    означает ошибку
    '''
    try:
        content: TextIOWrapper = open(requested_file, "r+")
    except:
        requested_file: str = "ErrorFileNotFound.txt"
        return requested_file
    content: TextIOWrapper = open(requested_file, "r+")
    returned_file: list = content.read().splitlines()
    return returned_file


def file_conversion(requested_file: str):
    '''
    Принимает название файла; пытается найти его и прочитать; если все условия выполнены, преобразовывает в нужный
    формат и возвращает список чисел; если условия не выполнены, возвращает ошибку
    :param requested_file: Название файла
    :return: Eсли файл соотвествует требованиям, возвращает преобразованный список чисел; если количество чисел в файле
    не соответствует первому значению, возвращает ошибку
    '''
    returned_file: list = read_file(requested_file)
    returned_file: list = list(map(int, returned_file))
    amount_of_numbers: int = returned_file[0]
    del returned_file[0]
    if amount_of_numbers == len(returned_file):
        return returned_file
    else:
        broken: str = "Количество чисел не соответствует первому значению"
        return broken

def error_checking(requested_file):
    '''
    Принимает название файла; проводит обнаружение ошибки; если находит, выводит текст с пояснением ошибки; если не
    находит ошибок, выводит итог работы функции file conversion(): (если файл соотвествует требованиям, возвращает
    преобразованный список чисел; если количество чисел в файле не соответствует первому значению, возвращает ошибку)
    :param requested_file: Название файла
    :return: Ошибку, если срабатывает except; итог работы функции file_conversion()
    '''
    if read_file(requested_file) == "ErrorFileNotFound.txt":
        print("Ошибка в имени файла")
    else:
        try:
            print(file_conversion(requested_file))
        except TypeError:
            print("Неверный тип принимаемых данных")
        except IndexError:
            print("Пустой файл")
        except ValueError:
            print("Неверный тип данных в файле, введите значения типа Int()")
        except FileNotFoundError:
            print("Такого файла нету")
        except:
            print("Неизвестная ошибка")
        finally:
            print("===========")