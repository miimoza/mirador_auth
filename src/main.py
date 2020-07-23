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
        id, data = RFID.read(reader)

        GPIO.output(greenlight_pin, GPIO.HIGH)
        print("button:" + str(button.button_pressed))
        if button.button_pressed:
            print("LE BOUTON A ETE PRESSEEEEE + SA A SCAN UNE CARTE BIENVU")
            user.create(id)
            button.button_pressed = False
            for i in range(0,200):
                GPIO.output(greenlight_pin, GPIO.LOW)
                GPIO.output(greenlight_pin, GPIO.HIGH)
                time.sleep(0.05)

        else:
            try:
                dict = user.get_info(id)
                user.increment_visit(id, dict)    
                display.pretty_print(dict)
            
            except Exception as e:
                GPIO.output(redlight_pin, GPIO.HIGH)
                print("[ERROR] ID not identified")
            
        display.wait_and_clear()

        GPIO.output(redlight_pin, GPIO.LOW)
        GPIO.output(greenlight_pin, GPIO.LOW)
        
        button_pressed = False

    GPIO.cleanup()

    

if __name__ == "__main__":
    main()
