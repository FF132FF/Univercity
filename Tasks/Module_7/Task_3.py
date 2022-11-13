elections = {}
N = int(input(" Введите число: "))

while N != 0:
    key = input(" Выберите кандидата: ")
    value = int(input(" Введите его голоса : "))
    if key not in elections:
        elections[key] = value
    else:
        elections[key] += value
    N -= 1

for i in sorted(elections.keys()):
    print(i, elections[i])
