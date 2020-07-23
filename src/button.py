from threading import Thread
import RPi.GPIO as GPIO
import RFID
import display
import user
import keyboard
import main

def button_wrapper(reader, pin):
    Thread(target = wrapper, args = (pin, button_callback, reader)).start()

def wrapper(gpio_number, function, reader):
    while True:
        r = GPIO.input(gpio_number)
        if r == False:
            function(reader)

def button_callback(reader):
    global main.button_pressed
    main.button_pressed = True
    print("waiting for new user to be registred...")
