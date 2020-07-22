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

    GPIO.setwarnings(True)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(gpio_number, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    reader = RFID.init_mfrc()

    while True:
        id, data = RFID.read(reader)
        button.button_wrapper(reader)
        dict = user.get_info(id)
        user.increment_visit(id, dict)
        display.pretty_print(dict)
        display.wait_and_clear()

    GPIO.cleanup()

if __name__ == "__main__":
    main()
