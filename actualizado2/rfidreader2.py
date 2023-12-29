import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import csv
from time import sleep


def read_rfid():
    reader = SimpleMFRC522()
    while True:
        try:
            card_id, _ = reader.read()
            # lee como int
            return card_id
        finally:
            GPIO.cleanup()


def find_file(hexcode):
    # devuelve lista de la fila

    with open("mecadb.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            if row[0] == str(hexcode):
                return row

    # **** Este codigo estaba demasiado god que me dio pena borrarlo, quizas lo use mas adelante ****
    # (es con pandas)
    # -> encuentra la fila (o filas) con el valor "x" en df['columna']
    # fila_delhex = df.loc[df['hex'] == hexcode]
    # -> coloca los valores de la fila en variables
    # h3x, obj, own, loc = [fila_delhex[row].tolist() for row in fila_delhex]
    # -> como las variables estan en listas y no me gusta las vuelvo not-listas
    # h3x, obj, own, loc = h3x[0], obj[0], own[0], loc[0]
    # -> stack overflow my beloved
    # return h3x, obj, own, loc


def main():
    while True:
        hexcode = read_rfid()
        sleep(1)
        list_row = find_file(hexcode)
        print(list_row)


# main
main()
