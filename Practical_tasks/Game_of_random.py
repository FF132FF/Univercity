import random

num_of_lives = 3
count = 0

while True:
    n1 = random.randint(0, 99)
    n2 = random.randint(0, 99)
    n3 = random.randint(0, 1)
    print("---------------------------------------------------------------------")
    print("Количество жизней = ", num_of_lives)
    if n3 == 0:
        n2 = n2*(-1)
        print("|", n1, n2, "=", "??? |")
    else:
        print("|", n1, "+", n2, "=", "??? |")
    a = int(input("ваш ответ: "))
    if a == (n1 + n2):
        count = count + 1
        print("Правильно, у вас есть еще попытка. А пока ваш текущий рекорд *", count, "*")
        continue
    elif num_of_lives == 3:
        num_of_lives -= 1
        print("Вы ошиблись и потеряли одну жизнь, но у вас их еще достаточно")
        continue
    elif num_of_lives == 2:
        num_of_lives -= 1
        print("Теперь у вас осталась всего одна жизнь, играйте осторожнее!")
        continue
    elif num_of_lives == 1:
        num_of_lives -= 1
        print("У вас закончились жизни. Если допустите ошибку, проиграете")
        continue
    elif num_of_lives == 0:
        print("Увы, но этот ответ неверен и ваша последняя жизнь тоже сгорела. Ваш рекорд составил:", count)
        break