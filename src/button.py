import GPIO

def button_wrapper():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    thread_button = Thread(target = wrapper, args = (18, button))

def wrapper(gpio_number, function):
    GPIO.setup(gpio_number, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    while True:
        r = GPIO.input(gpio_number)
        if r == False:
            function()
