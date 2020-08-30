#!/usr/bin/env python3

import RPi.GPIO as GPIO
import RFID
from threading import Thread
import user
import display
import os
import time
import button
import ranking_board

def main():
    os.system('clear')

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

    reader = RFID.init_mfrc()

    button.button_wrapper(reader, button_pin)

    while True:
        display.print_banner()
        ranking_board.dump()


        #================== WAIT FOR SOMEONE TO SCAN HIS CARD ==================
        display.print_n(0, 4, "SCAN YOU CARD...\n")
        id, data = RFID.read(reader)

        # Switch on the green light to notify the scan
        GPIO.output(greenlight_pin, GPIO.HIGH)

        if button.button_pressed:
            print("Creating the new profile...")
            user.create(id)
            button.button_pressed = False
        else:
            if user.id_exist(id):
                userinfo = user.get_info(id)
                user.increment_visit(id, userinfo)
                display.print_userinfo(userinfo)
            else:
                GPIO.output(redlight_pin, GPIO.HIGH)

                print("[ERROR] ID not identified")
                print("\nClick on the button then scan the ")
                print("card to create a new MMC.\n")
                print("(MMC: Mirador Member Card)")

        display.wait_and_clear()

        # Switch Off the lights
        GPIO.output(redlight_pin, GPIO.LOW)
        GPIO.output(greenlight_pin, GPIO.LOW)

        button_pressed = False

    GPIO.cleanup()



if __name__ == "__main__":
    main()
