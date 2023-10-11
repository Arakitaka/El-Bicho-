import sqlite3
import dbfunctions as de
import random


def coordenadas_random():
    return (str(round(random.uniform(90, -90), 3)), str(round(random.uniform(90, -90), 3)))
print(coordenadas_random())

conection = sqlite3.connect("rfiddatabase.db")
table = "RFID"
columnas_tuple = ("hexcode", "object", "owner", "location")

hexcode = input("hexcode >>> ")
object = input("object >>> ")
owner = input("owner >>> ")
location = coordenadas_random()
el_tuple = (hexcode, object, owner, location)

de.load_values(conection, table, columnas_tuple, el_tuple)
print("funco9170172472")

# teoricamente funca para poder subir los valores