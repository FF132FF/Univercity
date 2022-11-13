def read_file(requested_file):
    content = open(requested_file, "r+")
    returned_file = list(set(content.read().splitlines()))
    return returned_file

def save_file(returned_file, requested_file):
    content = read_file(requested_file)
    content.sort()
    count = len(content)
    words = content
    words = ' '.join(words)
    words = words.replace(" ", "\n")
    text_to_write = count, words
    returned_file = open(returned_file, mode='w+')
    returned_file.write(str(count))
    returned_file.write(str("\n===========\n"))
    returned_file.write(str(words))
    return returned_file