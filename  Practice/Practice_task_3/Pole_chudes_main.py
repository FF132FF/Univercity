import Fixing_a_record
import random

current_record: int = 0
dictionary: list = Fixing_a_record.get_word()
print("Dictionary pool: ", dictionary)
print(Fixing_a_record.fixing_a_record(current_record))
lifes: int = int(input("===(1) Easy difficulty level (7 lifes), \n===(2) Normal difficulty level (5 lifes), "
    "\n===(3) Hard difficulty level (3 lifes), \n===(or input == lifes!) \nEnter your chosen difficulty level: "))

if lifes == 1:
    lifes = 7
elif lifes == 2:
    lifes = 5
elif lifes == 3:
    lifes = 3

while len(dictionary) != 0:
    print("=============================================")
    print("Words in pool: ", len(dictionary))
    record: list = []
    hidden_word: list = []
    for i in range(0, len(dictionary)):
        record.append(i)
    random_word = int(random.choice(record))
    dictionary_word = list(dictionary[random_word])
    for i in dictionary_word:
        hidden_word.append('\u25A0')
    print("===== Debug: ", dictionary_word, "=====")
    while lifes > 0:
        print("lifes = ", lifes)
        print("try to guess the full word or a single letter: ", hidden_word)
        letters: str = input("Enter a letter or the full word: ")
        counter: int = 0
        for i in dictionary_word:
            if letters == i:
                hidden_word[counter] = str(letters)
                lifes += 1
            counter += 1
        lifes -= 1
        if str(letters) == str(dictionary[random_word]):
            print("\n===== Word guessed. Full word in one try ===== \n")
            current_record += 1
            print(Fixing_a_record.fixing_a_record(current_record), "\n")
            dictionary.pop(random_word)
            break
        if '\u25A0' not in hidden_word:
            print("\n===== Word guessed. The words in the dictionary are over ===== \n")
            current_record += 1
            print(Fixing_a_record.fixing_a_record(current_record), "\n")
            dictionary.pop(random_word)
            break
    breaker: str = input("If you want break, write 'No', for continue, write 'Yes': ")
    if breaker == "No":
        dictionary: list = []
