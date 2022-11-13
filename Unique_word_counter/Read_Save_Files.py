def read_file():
    opened_file = open('data.txt')
    word_list = list(set(opened_file.read().splitlines()))
    return word_list

def save_file(txt, word):
    words = read_file()
    words.sort()
    print(words)
    count = len(word)

    return count, words