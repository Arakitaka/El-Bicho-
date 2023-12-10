import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import pandas as pd

df = pd.read_csv('mecadb.csv')


class RFID:
    def read(self):
        reader = SimpleMFRC522()
        try:
            card_id, _ = reader.read()
            print(card_id)
            bolb = df.loc[df['hex'] == str(card_id)]
            for index, row in bolb.iterrows():
                print(index, row['Name'], row['HP'])

        finally:
            GPIO.cleanup()
