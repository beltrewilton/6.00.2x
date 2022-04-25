import random


def getEven():
    return random.choice(list(range(0, 99, 2)))

print(getEven())