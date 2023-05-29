import random


def match_checking(group: int, iterations: int):
    '''
    Функция принимает количество студентов в группе и количество итераций; проверяет совпадают ли хотябы у двух
    студентов дни рождения; Возвращает разделитель (весь вывод отображается внутри функции, поэтому возвращает его)
    группе; возвращает разделитель (весь вывод отображается внутри функции, поэтому возвращает разделитель)
    :param group: Количество студентов в группе
    :param times: Количество итераций
    :return: Разделитель
    '''
    number_of_iterations: int = iterations
    count_yes: int = 0
    count_no: int = 0
    separator: str = "==========="
    print(separator)
    while iterations != 0:
        was_match: str = "No"
        birthdays_list: list = [random.randint(1, 365) for i in range(group)]
        for i in range(0, len(birthdays_list)):
            if i != birthdays_list.index(birthdays_list[i]):
                was_match: str = "Yes"
        if was_match == "Yes":
            count_yes += 1
        else:
            count_no += 1
        iterations -= 1
    print("День рождения совпадают в", count_yes / (number_of_iterations / 100), "% случаев", "\nа не совпадают",
          count_no / (number_of_iterations / 100), "% случаев")
    return separator
