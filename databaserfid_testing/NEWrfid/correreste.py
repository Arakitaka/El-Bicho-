import dbfunctions
import sqlite3

table = "RFID"
columnas_tuple = ("ID", "hexcode", "object", "owner", "location")
conection = sqlite3.connect("rfiddatabase.db")


owo = ("id", "2", "2", "2", "2")

dbfunctions.load_values(conection, table, columnas_tuple, owo)

