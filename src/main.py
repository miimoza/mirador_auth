#!/usr/bin/env python3

import RPi.GPIO as GPIO
import RFID
from threading import Thread
import user
import display
import os
import time
import button

#button_pressed = False

def main():
    #global button_pressed

    os.system('clear')


    # BCM 18
    # BOARD 12
    button_pin = 16
    greenlight_pin = 20
    redlight_pin = 21
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    GPIO.setup(greenlight_pin, GPIO.OUT)
    GPIO.setup(redlight_pin, GPIO.OUT)
    GPIO.output(redlight_pin, GPIO.LOW)
    GPIO.output(greenlight_pin, GPIO.LOW)


    # RFID
    reader = RFID.init_mfrc()

    button.button_wrapper(reader, button_pin)

    while True:
        display.print_banner()

        id, data = RFID.read(reader)

        GPIO.output(greenlight_pin, GPIO.HIGH)

        if button.button_pressed:
            print("Creating the new profile...")
            user.create(id)
            button.button_pressed = False

        else:
            try:
                userinfo = user.get_info(id)
                user.increment_visit(id, userinfo)    
                display.print_userinfo(userinfo)
            
            except Exception as e:
                GPIO.output(redlight_pin, GPIO.HIGH)
                print(e)
                print("[ERROR] ID not identified")
                print("\nClick on the button then scan the ")
                print("card to create a new MMC.\n")
                print("(MMC: Mirador Member Card)")
            
        display.wait_and_clear()

        GPIO.output(redlight_pin, GPIO.LOW)
        GPIO.output(greenlight_pin, GPIO.LOW)
        
        button_pressed = False

    GPIO.cleanup()

    

if __name__ == "__main__":
    main()
