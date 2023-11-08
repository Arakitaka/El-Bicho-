import dbfunctions as df
import readerfunction as rr
import sqlite3

table = "RFID"
des_col = ("object", "owner", "location")
hex_col = "hexcode"
conection = sqlite3.connect("rfiddatabase.db")

while True:
    hex_val = rr.read_rfid()
    print(df.read_values(conection, table, "hexcode", hex_val, des_col))
