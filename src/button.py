from threading import Thread
import RPi.GPIO as GPIO
import RFID
import user

def button_wrapper():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    thread_button = Thread(target = wrapper, args = (18, button_callback))

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
            function()
