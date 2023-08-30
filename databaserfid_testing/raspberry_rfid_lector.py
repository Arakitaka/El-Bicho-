import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import sqlite3
from database_testing import database_editor as de

conection = sqlite3.connect("rfiddatabase.db")
table = "RFID"
column_value = "hexcode"


reader = SimpleMFRC522.SimpleMFRC522()
try:
    while True:
        card_id, card_text = reader.read()
        print(card_id)
        print(de.read_values(conection, table, column_value, card_id))
finally:
    GPIO.cleanup()

# tecnicamente este codigo serviria para mecatronica y metodologia, probar despues
