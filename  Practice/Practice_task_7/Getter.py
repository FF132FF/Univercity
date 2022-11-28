import csv

def csv_extract():
    '''
    Открывает файл books.csv и конвертирует его в читаемый для программы текст
    :return: текст без isbn|title|author|quantity|price
    '''
    with open('books.csv', 'r', ) as file:
        fixed_text = ""
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            fixed_text = fixed_text+str(row)+"\n"
    fixed_text = fixed_text.replace("[","").replace("]","").replace("'","")
    fixed_text = fixed_text.replace("isbn|title|author|quantity|price", "").replace("\n", "", 1)
    fixed_text = fixed_text[::-1].replace("\n", "", 1)
    fixed_text = fixed_text[::-1]
    return fixed_text

def convert_list():
    '''
    Преобразует текст в список, с маленькими буквами для удобства поиска в будущем
    :return: список
    '''
    txtfromfile = csv_extract()
    txt = txtfromfile.lower()
    txt = txt.splitlines()
    txt_out = txt
    c = 0
    for word in txt:
        txt_out[c] = txt[c]
        c += 1
    return txt_out


def get_name(name):
    '''
    Ищет по данному тексту совпадения, заносит их в список
    :param name: текст для поиска
    :return: список с совпадениями
    '''
    list = convert_list()
    new_li = []; c = 0
    for word in list:
        split_list = list[c].split("|")
        only_name = split_list[1]
        name = name.lower()
        if name in only_name.split():
            new_li.append(list[c])
        c += 1
    return new_li


def get_list(new_list):
    '''
    Оставляет первою строку, умножает количество на цену, помещает в список
    :param new_list: список для счета
    :return: новый умноженный список
    '''
    c = 0; newer_li = []
    for words in new_list:
        split_list = new_list[c].split("|")
        id = split_list[0]; amount = split_list[3]; cost = split_list[4]
        tempm = float(amount) * float(cost)
        split_list = id, tempm
        newer_li.append(split_list)
        c += 1
    return newer_li


def get_totals(newer_list):
    '''
    Функция, которая добавляет к сумме значение 100, если сумма меньше 500
    :param newer_list: список для считывания
    :return: список с измененными по условию значениями
    '''
    c = 0; newest_li = []
    for words in newer_list:
        current_part = newer_list[c]
        current_id = current_part[0]; temp1 = current_part[1]
        if temp1 < 500:
            temp1 += 100
        c += 1
        current_part = current_id, temp1
        newest_li.append(current_part)
    return newest_li

def printlist(list_name: list):
    '''
    Только для вывода списка
    :param list_name: список
    :return: выводит в консоль
    '''
    list_name = str(list_name).title()
    print(list_name)