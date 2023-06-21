import RPi.GPIO as GPIO
import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()
try:
    while True:
        card_id, card_text = reader.read()
        print(card_id)
        print(card_text)
finally:
    GPIO.cleanup()
