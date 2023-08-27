import sqlite3
from database_testing import database_editor as de
from meca_rfid.databaserfid_testing import doxxeo_epico as doxx

conection = sqlite3.connect("rfiddatabase.db")
table = "RFID"

hexcode = input("hexcode >>> ")
object = input("object >>> ")
owner = input("owner >>> ")
location = doxx.coordenadas_random()
el_tuple = (hexcode, object, owner, location)

de.load_values(conection, table, location)

# teoricamente funca para poder subir los valores