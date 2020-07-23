from threading import Thread
import RPi.GPIO as GPIO
import RFID
import display
import user
import keyboard
import main
import time

def button_wrapper(reader, pin):
    Thread(target = wrapper, args = (pin, button_callback, reader)).start()

def wrapper(gpio_number, function, reader):
    while True:
        r = GPIO.input(gpio_number)
        if r == False:
            r = True
            function(reader)
        time.sleep(0.1)

def button_callback(reader):
    main.button_pressed = True
    print("BOUTTON CLICK WAITING FOR CREATION")
