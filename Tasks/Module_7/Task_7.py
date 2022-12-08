l: list = []
N: int = int(input("Введите количество строк: "))

while N != 0:
    key: str = input()
    words: list = key.split(' ')
    for word in words:
        l.append(word)
    N -= 1

d: dict = {}

for i in l:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

d2: dict = dict(sorted(d.items()))
l2: list = sorted(d2, key=d2.get, reverse=True)

for el in l2:
    for key, value in d2.items():
        if el in key:
            print(el, value)
