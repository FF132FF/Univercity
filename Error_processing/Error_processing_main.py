import File_conversion

requested_file = str(input("Enter the name of the file to read and return data: "))
returned_file = File_conversion.read_file(requested_file)

try:
    print(File_conversion.file_conversion(requested_file))
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


