sentence = input()
words = sentence.split(' ')
l = []
result = {}
for word in words:
    result[word] = result.get(word, 0) + 1
    l.append(result.get(word, 0) - 1)
print(l)