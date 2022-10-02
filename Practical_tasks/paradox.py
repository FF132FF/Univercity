import random

def monty_hall(amount):
    total = amount
    selected_door_0 = 0
    selected_door_1 = 0
    while amount != 0:
        a = [0, 1, 0]
        c = random.choice(a)
        a = [0, 1]
        if c == 0:
            selected_door_1 += 1
        elif c == 1:
            selected_door_0 += 1
        amount -= 1
    return selected_door_1 / (total / 100)

def birthday(amount):
    return amount
