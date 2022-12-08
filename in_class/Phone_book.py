phone_book = {}


def menu_select():
    '''
    Выбор функции, которую хотим использовать; возвращает номер функции
    :param a: Параметр (изначально 0)
    :return: Параметр (1-4 в зависимости от выбранной функции)
    '''

    action: int = int(input("1 Добавить контакт \n2 Удалить контакт \n3 Изменить контакт \n4 Просмотреть контакты "
                            "\n0 Закрыть меню выбора функций \n==== "))
    return action


def contact_input():
    '''
    Записывает новый ключ (контакт)
    :return: Ключ
    '''
    key = str(input("Введите контакт: "))
    key = key.lower()
    key = key.title()
    return key


def num_input():
    '''
    Записывает значение для ключа; форматирует значение; проверяет число ли это; если нет, вызывает функцию заново;
    возвращает значение для ключа;
    :return: Значение (для ключа)
    '''
    value: str = input("Введите номер телефона: ")
    value = value.replace("+7", "8")
    value = value.replace(" ", "").replace("-", "")
    while value.isdigit() != 1:
        print("Введите снова")
        value = num_input()
    return value


def del_contact():
    '''
    Удаляет контакт; возвращает сообщение о том, что контакт удален
    :return: Сообщение (о том, что контакт удален)
    '''
    key = str(input("Введите контакт, который хотите удалить: "))
    del phone_book[key]
    return "==== Контакт удален ===="


def add_contact():
    '''
    Добавляет контакт; При помощи функций получает ключ(имя контакта), значение для ключа(номер телефона); Записывает
    ключ: значение в словарь phone_book; возвращает сообщение о том, что контакт добавлен
    :return: Сообщение (о том, что контакт добавлен)
    '''
    key: str = contact_input()
    value: str = num_input()
    phone_book[key] = value
    return "==== Контакт добавлен ===="


def change_contact():
    '''
    Изменяет телефон для контакта (значение для ключа в словаре); получаем ключ, и удаляем его; записываем заново с
    новым значением; возвращает сообщение о том, что контакт изменен
    :return: Сообщение (о том, что контакт изменен)
    '''
    print("==== Контакт, который хотите изменить ====")
    key: str = contact_input()
    del phone_book[key]
    print("==== Новый номер ====")
    value: str = num_input()
    phone_book[key] = value
    return "==== Контакт изменен ===="


action = menu_select()

while action != 0:
    if action == 1:
        add_contact()
    if action == 2:
        del_contact()
    if action == 3:
        change_contact()
    if action == 4:
        print(phone_book)
    action = menu_select()
