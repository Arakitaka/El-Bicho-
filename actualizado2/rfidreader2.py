import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import pandas as pd
from time import sleep

# Nota: el pandas solo lee el hex como int (amen)

df = pd.read_csv('mecadb.csv')


def read_rfid():
    reader = SimpleMFRC522()
    while True:
        try:
            card_id, _ = reader.read()
            print(card_id)
            return card_id
        finally:
            GPIO.cleanup()


def find_file(hexcode):
    # encuentra la fila (o filas) con el valor "x" en df['columna']
    fila_delhex = df.loc[df['hex'] == hexcode]
    # coloca los valores de la fila en variables
    h3x, obj, own, loc = [fila_delhex[row].tolist() for row in fila_delhex]
    # como las variables estan en listas y no me gusta las vuelvo not-listas
    h3x, obj, own, loc = h3x[0], obj[0], own[0], loc[0]
    # stack overflow my beloved
    return h3x, obj, own, loc


def main():
    while True:
        hexcode = read_rfid()
        sleep(1)
        tup_hool = find_file(hexcode)
        print(tup_hool)


# main
main()
