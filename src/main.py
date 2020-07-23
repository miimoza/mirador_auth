#!/usr/bin/env python3

import RPi.GPIO as GPIO
import RFID
from threading import Thread
import user
import display
import os
import time
import button

def main():
    os.system('clear')

    # BCM 18
    # BOARD 12
    button_pin = 16
    greenlight_pin = 20
    redlight_pin = 21
    GPIO.setwarnings(True)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    GPIO.setup(greenlight_pin, GPIO.OUT)
    GPIO.setup(redlight_pin, GPIO.OUT)

    # RFID
    reader = RFID.init_mfrc()

    button.button_wrapper(reader, button_pin)

    Thread(target = reader_loop, args = [reader]).start()

    GPIO.cleanup()

def reader_loop(reader):
    while True:
        id, data = RFID.read(reader)
        dict = user.get_info(id)
        user.increment_visit(id, dict)
        display.pretty_print(dict)
        display.wait_and_clear()

if __name__ == "__main__":
    main()
