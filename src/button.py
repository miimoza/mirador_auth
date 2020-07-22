from threading import Thread
import RPi.GPIO as GPIO
import RFID
import display
import user
import keyboard

def button_wrapper(reader, pin):
    Thread(target = wrapper, args = (pin, button_callback, reader)).start()

def wrapper(gpio_number, function, reader):
    while True:
        #r = GPIO.input(gpio_number)
        #if r == False:
        if keyboard.is_pressed('b'):
            function(reader)

def button_callback(reader):
    print("waiting for new user to be registred...")
    id, data = RFID.read(reader)
    user.create(id)
    display.wait_and_clear()
