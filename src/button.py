from threading import Thread
import RPi.GPIO as GPIO
import RFID
import display
import user

def button_wrapper():
    GPIO.setwarnings(True)
    GPIO.setmode(GPIO.BCM)
    Thread(target = wrapper, args = (18, button_callback)).start()

def button_callback():
    print("waiting for new user to be registred...")
    id, data = RFID.read()
    user.create(id)
    display.wait_and_clear()

def wrapper(gpio_number, function):
    GPIO.setup(gpio_number, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    while True:
        r = GPIO.input(gpio_number)
        if r == False:
            GPIO.cleanup()
            function()
