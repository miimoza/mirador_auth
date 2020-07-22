#!/usr/bin/env python3

import RPi.GPIO as GPIO
import RFID
import user
import display
import os
import keyboard
import time
import button

def main():
    os.system('clear')
    while True:
        GPIO.cleanup()
        GPIO.setwarnings(True)
        GPIO.setmode(GPIO.BCM)
        id, data = RFID.read()
        button.button_wrapper()
        dict = user.get_info(id)
        user.increment_visit(id, dict)
        display.pretty_print(dict)
        display.wait_and_clear()

if __name__ == "__main__":
    main()
