files_with_them_operations = {}
number_of_files = int(input("Введите число строк (количество файлов в файловой системе): "))

while number_of_files != 0:
    files_names_operations = input("Введите название файла и доступные ему операции через пробел: ")
    key = files_names_operations.split(" ", 1)
    key2 = str(key[:1])[2:-2]

    value2 = str(key[1:])
    value2 = str(value2.split())
    value3 = list(value2)

    files_with_them_operations[key2] = value3
    number_of_files -= 1

availability_of_operations = []
number_of_operations = int(input("Введите количество операций с файлами, которое хотели бы произвести: "))

while number_of_operations != 0:
    operation_file_name = input("Введите операцию и имя файла с которым хотели бы произвести эту операцию, через пробел: ")
    key = operation_file_name.split(" ", 1)
    key2 = str(key[:1])[2:-2]
    value = operation_file_name.split(" ", 1)
    value2 = str(key[1:])[2:-2]

    match key2:
        case 'read':
            if 'R' in files_with_them_operations[value2]:
                availability_of_operations.append("Ok")
            else:
                availability_of_operations.append("Denied")
        case 'write':
            if 'W' in files_with_them_operations[value2]:
                availability_of_operations.append("Ok")
            else:
                availability_of_operations.append("Denied")
        case 'execute':
            if 'E' in files_with_them_operations[value2]:
                availability_of_operations.append("Ok")
            else:
                availability_of_operations.append("Denied")

    number_of_operations -= 1

for i in availability_of_operations:
    print (i)
