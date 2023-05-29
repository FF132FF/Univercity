import File_conversion

requested_file: str = str(input("Enter the name of the file to read and return data: "))
File_conversion.error_checking(requested_file)

#   data.txt; dataNull.txt; broken.txt; txt.txt - файлы для проверки работы функции с ошибками
