string_of_letters = input()
list_of_letters_1 = list(string_of_letters)
list_of_letters_2 = list_of_letters_1[0: (list_of_letters_1.index("h") + 1)]
list_of_letters_1.reverse()
list_of_letters_3 = list_of_letters_1[0: (list_of_letters_1.index("h") + 1)]
list_of_letters_3.reverse()
list_of_letters_5 = list_of_letters_1.copy()
list_of_letters_1.reverse()
list_of_letters_4 = list_of_letters_1[list_of_letters_5.index("h"): (len(list_of_letters_1) - (list_of_letters_1.index("h") + 2))]
list_of_letters_4.reverse()
list_of_letters_2.append("".join(map(str, list_of_letters_4)))
list_of_letters_2.append("".join(map(str, list_of_letters_3)))
print("".join(map(str, list_of_letters_2)))
