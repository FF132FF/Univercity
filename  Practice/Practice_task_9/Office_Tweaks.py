import os
import pathlib
import time
import re
from pdf2docx import parse
from docx2pdf import convert
from PIL import Image


def change_working_directory():
    '''
    Проверяет существует ли каталог; если существует, то изменяет текущий католог; затем возврат к функции action_choice
    '''
    path: str = str(input("=== Укажите корректный путь к рабочему катологу: "))
    if os.path.exists(path) is True:
        print("=== Переход в директорию ===")
        os.chdir(path)
        action_choice()
    else:
        print("=== Такого пути не существует ===")
        change_working_directory()


def converter(choice):
    '''
    Выводит все файлы с расширением pdf; возвращает два списка: один со списками всех пдф файлов, другой с полными
    путями к ним; дает выбор: преобразовать один файл или сразу все
    :return: 2 списка
    '''
    this_directory: str = os.getcwd()
    print("=== Список файлов с расширением pdf в текущем каталоге", this_directory)
    get_all_items: list = os.listdir(os.getcwd())
    list_for_pdf: list = []
    list_for_doc: list = []
    list_for_path: list = []
    i = 0
    j = 0
    if choice == 1:
        for word in get_all_items:
            if pathlib.Path(word).suffix == ".pdf":
                i += 1
                list_for_pdf.append(word)
                list_for_path.append(os.path.abspath(word))
                print(i, word)
        number_of_file = int(input("=== Ваш выбор (введите 0, если хотите преобразовать все файлы): "))
        if number_of_file == 0:
            i = 1
            for word in list_for_pdf:
                selected_path: str = list_for_path[i - 1]
                selected_pdf: str = list_for_pdf[i - 1]
                future_doc: str = selected_pdf + ".doc"
                future_doc: str = future_doc.replace('.pdf', '')
                parse(selected_path, future_doc)
                time.sleep(1)
                i += 1
            print("=== Все файлы преобразованы ===")
            action_choice()
        else:
            selected_path: str = list_for_path[number_of_file - 1]
            selected_pdf: str = list_for_pdf[number_of_file - 1]
            future_doc: str = selected_pdf + ".doc"
            future_doc: str = future_doc.replace('.pdf', '')
            parse(selected_path, future_doc)
            time.sleep(1)
            action_choice()
    elif choice == 2:
        for word in get_all_items:
            if pathlib.Path(word).suffix == ".doc" or pathlib.Path(word).suffix == ".docx":
                j += 1
                list_for_doc.append(word)
                list_for_path.append(os.path.abspath(word))
                print(j, word)
        number_of_file = int(input("=== Ваш выбор (введите 0, если хотите преобразовать все файлы): "))
        if number_of_file == 0:
            j = 1
            for word in list_for_doc:
                selected_path: str = list_for_path[j - 1]
                selected_pdf: str = list_for_doc[j - 1]
                future_doc: str = selected_pdf + ".pdf"
                future_doc: str = future_doc.replace('.docx', '').replace('.doc', '')
                convert(selected_path, future_doc)
                time.sleep(1)
                j += 1
            print("=== Все файлы преобразованы ===")
            action_choice()
        else:
            selected_path: str = list_for_path[number_of_file - 1]
            selected_pdf: str = list_for_doc[number_of_file - 1]
            future_doc: str = selected_pdf + ".pdf"
            future_doc: str = future_doc.replace('.docx', '').replace('.doc', '')
            convert(selected_path, future_doc)
            time.sleep(1)
            action_choice()


def compress_images():
    '''
    Выводит все файлы с расширением jpg/gif/png/jpeg; возвращает два списка: один со списками всех картинок, другой с
    полными путями к ним; дает выбор: преобразовать один файл, или сразу все
    '''
    this_directory: str = os.getcwd()
    print("=== Список файлов с расширением jpg, png, gif, jpeg в текущем каталоге", this_directory)
    get_all_items: list = os.listdir(os.getcwd())
    list_for_img: list = []
    list_for_path: list = []
    i = 0
    for word in get_all_items:
        if pathlib.Path(word).suffix == ".jpg" or pathlib.Path(word).suffix == ".png" or \
                pathlib.Path(word).suffix == ".gif" or pathlib.Path(word).suffix == ".jpeg":
            i += 1
            list_for_img.append(word)
            list_for_path.append(os.path.abspath(word))
            print(i, ". ", word)
    choice = int(input("=== Ваш выбор (введите 0, если хотите преобразовать все файлы): "))
    if choice == 0:
        i = 1
        qualityMy = int(input("=== Ведите качество сжатия (0-100): "))
        for word in list_for_img:
            selected_path: str = list_for_path[i - 1]
            selected_img: str = list_for_img[i - 1]
            image_open: PIL.JpegImagePlugin.JpegImageFile = Image.open(selected_path)
            future_name: str = "(quality " + str(qualityMy) + ")" + selected_img
            image_open.save(future_name, quality=qualityMy)
            time.sleep(1)
            i += 1
        print("\n=== Все файлы сжаты ===\n")
        action_choice()
    else:
        qualityMy = int(input("=== Ведите качество сжатия (0-100) : "))
        selected_path: str = list_for_path[choice - 1]
        selected_img: str = list_for_img[choice - 1]
        image_open: PIL.JpegImagePlugin.JpegImageFile = Image.open(selected_path)
        future_name: str = "(quality " + str(qualityMy) + ")" + selected_img
        image_open.save(future_name, quality=qualityMy)
        time.sleep(1)
        action_choice()


def deleting_a_group_of_files():
    '''
    Выводит все файлы из текущей папки; предлагает выбор; в зависимости от этого выбора ищет по патерну, затем выводит
    то, что удалил и что осталось после
    '''
    get_all_items: list = os.listdir(os.getcwd())
    print("Текущие файлы из ", os.getcwd(), " : ", get_all_items)
    print("\n1. Удалить все файлы начинающиеся на определенную подстроку"
          "\n2. Удалить все файлы заканчивающиеся на определенную подстроку"
          "\n3. Удалить все файлы содержащие определенную подстроку"
          "\n4. Удалить все файлы по расширению")
    choice = int(input("\nВаш выбор: "))
    if choice == 1:
        directory: str = os.getcwd()
        files_in_directory: list = os.listdir(directory)
        patternOrigin: str = input("=== Выберите подстроку начала: ")
        pattern: str = "^" + patternOrigin
        filtered_files: list = [file for file in files_in_directory if (re.search(pattern, file))]
        for file in filtered_files:
            if file.startswith(patternOrigin):
                path_to_file = os.path.join(directory, file)
                print("=== Удалено: ", path_to_file)
                os.remove(path_to_file)
        get_all_items: list = os.listdir(os.getcwd())
        print("==== Текущие файлы из ", os.getcwd(), " : ", get_all_items)
        action_choice()
    elif choice == 2:
        directory: str = os.getcwd()
        files_in_directory: list = os.listdir(directory)
        patternOrigin: str = input("=== Выберите подстроку окончания: ")
        pattern: str = patternOrigin + ".\w+$"
        filtered_files: list = [file for file in files_in_directory if (re.search(pattern, file))]
        for file in filtered_files:
            suffix: str = pathlib.Path(file).suffix
            fileFix: str = file.replace(suffix, "")
            if fileFix.endswith(patternOrigin):
                path_to_file = os.path.join(directory, file)
                print("=== Удалено: ", path_to_file)
                os.remove(path_to_file)
        get_all_items: list = os.listdir(os.getcwd())
        print("=== Текущие файлы из ", os.getcwd(), " : ", get_all_items)
        action_choice()
    elif choice == 3:
        directory: str = os.getcwd()
        files_in_directory: list = os.listdir(directory)
        pattern: str = input("=== Выберите подстроку по всем: ")
        filtered_files: list = [file for file in files_in_directory if (re.search(pattern, file))]
        for file in filtered_files:
            path_to_file = os.path.join(directory, file)
            print("=== Удалено: ", path_to_file)
            os.remove(path_to_file)
        get_all_items: list = os.listdir(os.getcwd())
        print("=== Текущие файлы из ", os.getcwd(), " : ", get_all_items)
        action_choice()
    elif choice == 4:
        directory: str = os.getcwd()
        files_in_directory: list = os.listdir(directory)
        pattern: str = input("=== Выберите подстроку расширения(без точки): ")
        pattern: str = pattern + "$"
        filtered_files: list = [file for file in files_in_directory if (re.search(pattern, file))]
        for file in filtered_files:
            path_to_file = os.path.join(directory, file)
            print("=== Удалено: ", path_to_file)
            os.remove(path_to_file)
        get_all_items: list = os.listdir(os.getcwd())
        print("=== Текущие файлы из ", os.getcwd(), " : ", get_all_items)
        action_choice()
    else:
        print("=== Введите число от 1 до 4")
        deleting_a_group_of_files()


def action_choice():
    '''
    Основная функция, которая обращается ко всем остальным; функция выбора действия и в зависимости от выборы вызывает
    другую функцию; бесконечный цикл действий, пока не выбрать действие 5 -> выход
    :return: пустой return
    '''
    print("\n=== Текущий католог:", os.getcwd())
    print("\n=== Выберите действие: ")
    print("\n0. Сменить рабочий каталог \n1. Преобразовать PDF в Docx \n2. Преобразовать Docx в PDF"
          "\n3. Произвести сжатие изображения \n4. Удалить группу файлов \n5. Выход")
    choice: int = int(input("\n=== Ваш выбор: "))
    if choice == 0:
        change_working_directory()
    if choice == 1:
        converter(choice)
    if choice == 2:
        converter(choice)
    if choice == 3:
        compress_images()
    if choice == 4:
        deleting_a_group_of_files()
    if choice == 5:
        return
