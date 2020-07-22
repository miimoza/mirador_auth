#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

def read():
    reader = SimpleMFRC522()
    try:
            id, data = reader.read()

            print("id:" + str(id))
            print("data:" + data)
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