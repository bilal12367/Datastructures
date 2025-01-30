import random

def genArr(count, rng):
    arr = []
    for i in range(count):
        arr.append(random.randint(1, rng))
    return arr