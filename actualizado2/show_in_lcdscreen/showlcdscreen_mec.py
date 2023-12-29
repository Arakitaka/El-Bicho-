import drivers
# drivers es una carpeta con lo complicado y tembo
# fuente: https://github.com/the-raspberry-pi-guy/lcd
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import csv


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


def show_screen(row_hex):
    # ! /usr/bin/env python

    # Simple string program. Writes and updates strings.
    # Demo program for the I2C 16x2 Display from Ryanteck.uk
    # Created by Matthew Timmons-Brown for The Raspberry Pi Guy YouTube channel

    # Import necessary libraries for communication and display use

    # Load the driver and set it to "display"
    # If you use something from the driver library use the "display." prefix first
    display = drivers.Lcd()
    # Main body of code
    obj = row_hex[1]
    owner = row_hex[2]
    line1 = f"Obj: {obj}"
    line2 = f"Owner: {owner}"

    try:
        display.lcd_clear()
        # max 16 characters
        display.lcd_display_string(string=line1, line=1)  # Write line of text to first line of display
        # (max 2 lines)
        display.lcd_display_string(string=line2, line=2)
    except KeyboardInterrupt:
        display.lcd_clear()


def main():
    hexc_old = None
    while True:
        hexcode = read_rfid()
        if hexcode != hexc_old:
            print(hexcode)
            list_row = find_file(hexcode)
            print("mostrando en pantalla...")
            show_screen(list_row)
            hexc_old = hexcode


if __name__ == "__main__":
    main()
