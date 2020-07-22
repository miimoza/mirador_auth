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
        dict = user.get_info(id)
        user.increment_visit(id, dict)
        display.pretty_print(dict)
        display.wait_and_clear()

    GPIO.cleanup()

if __name__ == "__main__":
    main()
