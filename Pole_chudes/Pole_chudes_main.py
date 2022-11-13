import Pole_chudes.FixRec as rec
import random

Record = 0
Current_Record = 0
Dictionary = []
Dictionary = rec.Get_Word()
print("Dictionary pool: ", Dictionary)

print(rec.Fix_a_Rec(Current_Record))
print("\n       Выборерите уровень сложности: ")

lifes = int(input("\n1 Easy difficulty level (7 lifes), 2 Normal difficulty level (5 lifes), 3 Hard difficulty level (3 lifes), or input == lifes!Enter your chosen difficulty level: "))
if lifes == 1:
    lifes = 7
elif lifes == 2:
    lifes = 5
elif lifes == 3:
    lifes = 3

while len(Dictionary) != 0:
    print("===========================================================================================================")
    print("\nWords in pool: ", len(Dictionary))
    Record = []
    hidden_word = []
    for i in range(0, len(Dictionary)):
        Record.append(i)
    f = int(random.choice(Record))
    Dictionary_Word = list(Dictionary[f])
    for i in Dictionary_Word:
        hidden_word.append('\u25A0')
    print("===== Debug: ", Dictionary_Word, "=====")

    while lifes > 0:
        print("lifes = ", lifes)
        print("try to guess the full word or a single letter: ", hidden_word)
        letters = input("Enter a letter or the full word: ")
        k = 0
        for i in Dictionary_Word:
            if letters == i:
                hidden_word[k] = str(letters)
                lifes += 1
            k += 1
        lifes -= 1
        if str(letters) == str(Dictionary[f]):
            print("\n ===== Word guessed. Full word in one try ===== \n")
            Current_Record += 1
            print(rec.Fix_a_Rec(Current_Record), "\n")
            Dictionary.pop(f)
            break
        if '\u25A0' not in hidden_word:
            print("\n ===== Word guessed. The words in the dictionary are over ===== \n")
            Current_Record += 1
            print(rec.Fix_a_Rec(Current_Record), "\n")
            Dictionary.pop(f)
            break
    breaker = input("Для остановки напишите 'No', для продолжения 'Yes': ")
    if breaker == "нет":
        Dictionary = []