#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

def read():
    reader = SimpleMFRC522()
    try:
            print("waiting for a card to be scanned...")
            id, data = reader.read()
            print("scanned id {}".format(id))
    finally:
            GPIO.cleanup()

    return (id, data)

def write(data):
    reader = SimpleMFRC522()
    try:
            reader.write(data)
            print("Written (data:"+ data + ")")
    finally:
            GPIO.cleanup()

def get_id(data):
    print("get_id")
