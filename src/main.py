#!/usr/bin/env python3

import RFID
import user
import display
import os
import keyboard
import time
import button

def main():
    os.system('clear')
    button.button_wrapper()
    while True:
        id, data = RFID.read()
        dict = user.get_info(id)
        user.increment_visit(id, dict)
        display.pretty_print(dict)
        display.wait_and_clear()

if __name__ == "__main__":
    main()
