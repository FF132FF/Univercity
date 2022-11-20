l = []
N = int(input("Введите количество строк: "))

while N != 0:
    key = input()
    words = key.split(' ')
    for word in words:
        l.append(word)
    N -= 1

d = {}

for i in l:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

d2 = dict(sorted(d.items()))
l2 = sorted(d2, key=d2.get, reverse=True)

for el in l2:
    for key, value in d2.items():
        if el in key:
            print(el, value)
