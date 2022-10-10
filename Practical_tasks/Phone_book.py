phone_book = {}

def input_command():
    print('1 - если вы хотите добавить контакт \n2 - если вы хотите удалить контакт \n3 - если вы хотите посмотреть контакты \n4 - если хотите изменить контакт \n5 - если хотите выйти')
    n = input('Введите номер команды, из списка: ')
    while not n.isdigit():
        print('Введите число:')
        n = input('Введите номер команды, из списка: ')
        return int(n)

def input_number():
    number = input('Введите телефон: ')
    number = number.replace('-', '').replace(' ', '')
    if number.isdigit and len(number) == 11:
        return number.replace('8', '+7', 1)
    else:
        return 0

def input_name():
    print('Введите имя:')
    name = input()
    if not name == '':
        return name.title()
    else:
        return 0

while True:
    n = input_command()
    if n == 1:
        number = input_number()
        name = input_name()
        while name == 0:
            print('Имя введено неверно')
            name = input_name()
        while number == 0:
            print('Номер введен неверно')
            number = input_number()
            phone_book[name] = number
    elif n == 2:
        name = input_name()
        while name == 0:
            print('Имя введено неверно')
            number = input_number()
        while not phone_book.__contains__(name):
            print('Такого контакта нет')
            name = input_name()
            phone_book.pop(name)
            print(f'Контакт {name} удален')
    elif n == 3:
        print(*phone_book.items())
    elif n == 4:
        name = input_name()
        while name == 0:
            print('Имя не верно')
            number = input_number()
        while not phone_book.__contains__(name):
            print('Такого контакта нет')
            name = input_name()
            number = input_number()
            while number == phone_book[name]:
                print(f'Вы ввели тот же самый номер')
                number = input_number()
                phone_book[name] = number
                print(f'Контакт {name} изменен')
    elif n == 5:
        break