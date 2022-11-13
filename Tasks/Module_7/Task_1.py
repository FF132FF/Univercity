text = input()
words = text.split(' ')
list = []
result = {}
for word in words:
    result[word] = result.get(word, 0) + 1
    list.append(result.get(word, 0) - 1)
print(*list, sep = ' ')