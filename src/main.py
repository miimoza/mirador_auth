#!/usr/bin/env python3

import RFID
import user
import display
import os
import keyboard
import time

def main():
    os.system('clear')
    print("BONJOUR MIRADOR")
    while True:
        if keyboard.is_pressed('c'):
            new_id = user.create(0)
            display.wait_and_clear()

        if keyboard.is_pressed('s'):
            id, data = RFID.read()
            dict = user.get_info(id)
            user.increment_visit(id, dict)
            display.pretty_print(dict)
            display.wait_and_clear()

if __name__ == "__main__":
    main()
