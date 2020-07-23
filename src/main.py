#!/usr/bin/env python3

import RPi.GPIO as GPIO
import RFID
from threading import Thread
import user
import display
import os
import time
import button

global button_pressed
button_pressed = False

def main():
    button_pressed = False

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

    while True:
        id, data = RFID.read(reader)
        print("button:" + str(button_pressed))
        if button_pressed:
            button_pressed = False
            user.create(id)
        else:
            try:
                dict = user.get_info(id)
                user.increment_visit(id, dict)    
                display.pretty_print(dict)
            
            except Exception as e:
                print("[ERROR] ID not identified")
            
        display.wait_and_clear()
        button_pressed = False

    GPIO.cleanup()

    

if __name__ == "__main__":
    main()
