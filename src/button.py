from threading import Thread
import RPi.GPIO as GPIO
import RFID
import display
import user
import main
import time

button_pressed = False

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
    global button_pressed
    if not button_pressed:
        button_pressed = True
        print("\nNOW SCAN YOUR CARD ON THE READER..\n")
