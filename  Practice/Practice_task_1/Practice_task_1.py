import random


def monty_hall_paradox(iterations: int):
    '''
    Функция принимает количество итераций проверяет и доказывает: правда ли, что вероятность победы увеличится при
    принятии предложения ведущего перевыбрать дверь; а так же можно проверить какой будет вероятность победы, если не
    принимать предложение ведущего и не менять дверь. Возвращает разделитель (весь вывод отображается внутри функции,
    поэтому такой return).
    :param iterations: Принимает количесвто итераций
    :return: Возвращает разделитель
    '''
    count_of_iterations: int = iterations
    selected_door_0_counter: int = 0
    selected_door_1_counter: int = 0
    swap = int(input('Если вы хотите узнать шанс победы,  при котором ваш выбор \nпостоянно изменяется и вы '
                     'перевыбираете дверь, напишите 1; \nне изменяется и вы не перевыбираете дверь напишите 0: '))
    separator: str = "=========="
    print(separator)
    while iterations != 0:
        behind_door_list: list = [0, 1, 0]
        selected_door: int = random.choice(behind_door_list)
        if selected_door == 0:
            if swap == 1:
                selected_door_1_counter += 1
            else:
                selected_door_0_counter += 1
        elif selected_door == 1:
            if swap == 1:
                selected_door_0_counter += 1
            else:
                selected_door_1_counter += 1
        iterations -= 1
    if swap == 1:
        choice: str = 'Да'
    else:
        choice: str = 'Нет'
    print("Изменяем наш выбор =", choice, "\nВероятность победы:",
          selected_door_1_counter / (count_of_iterations / 100),
          "\nВероятность поражения:", selected_door_0_counter / (count_of_iterations / 100))
    return separator


print(monty_hall_paradox(10000))
