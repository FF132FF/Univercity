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
    returned_file = open(returned_file, mode='w+')
    returned_file.write(str("# File content "))
    returned_file.write(str(returned_file.name))
    returned_file.write(str("\nTotal unique words: "))
    returned_file.write(str(count))
    returned_file.write(str("\n===========\n"))
    returned_file.write(str(words))
    return returned_file
