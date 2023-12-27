import random


def coordenadas_random():
    print(round(random.uniform(90, -90), 3), round(random.uniform(90, -90), 3))


for i in range(10):
    coordenadas_random()
