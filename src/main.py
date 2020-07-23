#!/usr/bin/env python3

import RPi.GPIO as GPIO
import RFID
from threading import Thread
import user
import display
import os
import time
import button

button_pressed = False

def main():
    global button_pressed

    os.system('clear')

    # BCM 18
    # BOARD 12
    button_pin = 18
    GPIO.setwarnings(True)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    # RFID
    reader = RFID.init_mfrc()

    button.button_wrapper(reader, button_pin)

    while True:
        id, data = RFID.read(reader)
        if button_pressed:
            user.create(id)
        else:
            dict = user.get_info(id)
            user.increment_visit(id, dict)
            display.pretty_print(dict)
        display.wait_and_clear()
        button_pressed = False

    GPIO.cleanup()

def reader_loop(reader):
    

if __name__ == "__main__":
    main()
