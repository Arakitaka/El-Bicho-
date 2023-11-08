import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522


def read_rfid():
    reader = SimpleMFRC522()
    try:
        card_id, _ = reader.read()
        return card_id
    finally:
        GPIO.cleanup()
