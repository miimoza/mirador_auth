from threading import Thread
import RPi.GPIO as GPIO
import RFID
import display
import user

def button_wrapper(reader):
    # BCM 18
    # BOARD 12
    Thread(target = wrapper, args = (12, button_callback, reader)).start()

def wrapper(gpio_number, function, reader):
    GPIO.setwarnings(True)
    while True:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(gpio_number, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        r = GPIO.input(gpio_number)
        if r == False:
            function(reader)

def button_callback(reader):
    print("waiting for new user to be registred...")
    id, data = RFID.read(reader)
    user.create(id)
    display.wait_and_clear()
