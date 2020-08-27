#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import sys

def init_mfrc():
    return SimpleMFRC522()

def read(reader):
    print("waiting for a card to be scanned...\n")
    reader = SimpleMFRC522()

    save_stdout = sys.stdout
    sys.stdout = open('trash', 'w')

    id, data = reader.read()

    sys.stdout = save_stdout


    return (id, data)

def write(reader, data):
    reader.write(data)
    print("Written (data:"+ data + ")")

def get_id(data):
    print("get_id")
