import random

def match_checking(group, times):
    times_fix = times
    count = 0
    while times != 0:
        coincided = "No"
        birth_days = [random.randint(1, 365) for i in range(0, group)]
        for i in range(0, len(birth_days)):
            if i != birth_days.index(birth_days[i]):
                coincided = "Yes"
        if coincided == "Yes":
            count += 1
        times -= 1
    return count / (times_fix / 100)

