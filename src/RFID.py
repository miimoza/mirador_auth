#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

def init_mfrc():
    return SimpleMFRC522()

def read(reader):
    print("waiting for a card to be scanned...")
    reader = SimpleMFRC522()
    id, data = reader.read()
    print("scanned id {}".format(id))

    return (id, data)

def write(reader, data):
    reader.write(data)
    print("Written (data:"+ data + ")")

def get_id(data):
    print("get_id")
