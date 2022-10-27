phone_book = {}
a = 0
key = str
temp = str
value = "123"

def menuSelect(a):
    a = int(input(" 1 Добавить контакт \n 2 Удалить контакт \n 3 Изменить контакт \n 4 просмотреть контакты \n "))
    return a

def name_input(key):
    key = input(" Введите контакт: ")
    key = key.lower()
    key = key.title()
    return key

def num_stand(temp):
    value = input(" Введите номер телефона: ")
    value = value.replace("+7", "8")
    value = value.replace(" ", "").replace("-", "")
    temp = value
    return temp

def num_input(value):
    value = num_stand(temp)
    while value.isdigit() != 1:
        print("Введите снова")
        value = num_stand(temp)
    return value

def deletionOf(key):
    key = "a"
    print(" Введите контакт, который хотите удалить: ")
    key = name_input(key)
    del phone_book[key]

def selected1(key,value):
    key = name_input(key)
    value = num_input(value)
    phone_book[key] = value

def selected3(key,value):
    print(" Введите контакт для изменения: ")
    key = name_input(key)
    del phone_book[key]
    print(" Введите новый номер: ")
    value = num_input(value)
    phone_book[key] = value

a = menuSelect(a)

while a != 0:
    if a == 1:
        selected1(key,value)
    if a == 2:
        deletionOf(key)
    if a == 3:
        selected3(key,value)
    if a == 4:
        print(phone_book)
    a = menuSelect(a)