#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

def read():
    reader = SimpleMFRC522()

    try:
            id, text = reader.read()
            print(id)
            print(text)
    finally:
            GPIO.cleanup()

def write():
    reader = SimpleMFRC522()

    try:
            text = input('New data:')
            print("Now place your tag to write")
            reader.write(text)
            print("Written")
    finally:
            GPIO.cleanup()

def get_id(data):
    print("get_id")
