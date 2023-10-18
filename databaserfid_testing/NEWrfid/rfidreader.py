import RPi.GPIO a GPIO
from mfrc522 import SimpleMFRC52
import sqlite3
import dbfunctions as db

conection = sqlite3.connect("rfiddatabase.db")
table = "RFID"
columnas_tuple = ("hexcode", "object", "owner", "location")


reader = SimpleMFRC52()
try:
    card_id, card_text = reader.read()
    print(card_id)
    db.read_values(conection, table, "hexcode", card_id, columnas_tuple)
finally:
    GPIO.cleanup()