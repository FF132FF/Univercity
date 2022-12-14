import re
import pymorphy2
from translate import Translator

translator = Translator(from_lang="ru", to_lang="en")
morph = pymorphy2.MorphAnalyzer()


def get_normal_form():
    '''
    Открывает и считыавет файл 'dialog.txt'; Переводит все буквы слов в нижний регистр; Отбирает по паттерну именно
    слова (убирает цифры и лишние символы); возвращает список этих слов
    :return: список (список слов без цифр и лишних символов)
    '''
    requested_file: TextIOWrapper = open('dialog.txt', mode='r+', encoding='utf-8')
    content: str = requested_file.read()
    content: str = content.lower()
    good_chars_pattern: str = r"(?:\я|\w+[^(\W|\d)]+)"
    match_words: list = re.findall(good_chars_pattern, content)
    return match_words


def get_dict():
    '''
    Обращается к функции get_normal_form(); получает оттуда список слов; преобразует список в словарь (ключ - слово,
    значение - количество встречающихся повторов слова); возвращает словарь
    :return: словарь
    '''
    list_of_words: list = get_normal_form()
    dict_of_words: dict = {}

    for word in list_of_words:
        if word in dict_of_words:
            dict_of_words[word] += 1
        else:
            dict_of_words[word] = 1

    return dict_of_words


def translation_and_formating():
    '''
    Обращается к функции get_dict(); получает оттуда словарь слов; сортирует, нормализирует и переводит список и словарь;
    записывает в файл 'word_translation.txt'; возвращает сообщение об окончании работы
    :return: Сообщение об окончании работы
    '''
    dict_of_words: dict = get_dict()
    sorted_dict_of_words: dict = dict(sorted(dict_of_words.items()))
    sorted_list_of_words: list = sorted(sorted_dict_of_words, key=sorted_dict_of_words.get, reverse=True)
    result_file = open('word_translation.txt', mode='w+', encoding='utf-8')

    for word in sorted_list_of_words:
        for key, value in sorted_dict_of_words.items():
            if word == key:
                morph_word: pymorphy2.analyzer.Parse = morph.parse(word)[0]
                word: str = morph_word.normal_form
                word_translated: str = translator.translate(word)
                result_file.write(str(word))
                result_file.write("|")
                result_file.write(str(word_translated))
                result_file.write("|")
                result_file.write(str(value))
                result_file.write('\n')

    return "\n===Данные отформатированы и сохранены в указанный файл===\n"
