import random


def coordenadas_random():
    return (round(random.uniform(90, -90), 3)), str(round(random.uniform(90, -90), 3))


print(coordenadas_random())

hexcode = input("hexcode >>> ")
objecto = input("object >>> ")
owner = input("owner >>> ")
location = coordenadas_random()
el_lista = (hexcode, objecto, owner, str(location))
print(el_lista)

append_list_as_row(el_lista)
print("funco")
