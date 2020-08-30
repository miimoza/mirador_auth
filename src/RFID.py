#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

def init_mfrc():
    return SimpleMFRC522()

def read(reader):
    reader = SimpleMFRC522()
    id, data = reader.read()

    return (id, data)

def write(reader, data):
    reader.write(data)
