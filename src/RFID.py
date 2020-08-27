#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import sys
import os

def init_mfrc():
    return SimpleMFRC522()

def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:
            yield
        finally:
            sys.stdout = old_stdout


def read(reader):
    print("waiting for a card to be scanned...\n")
    reader = SimpleMFRC522()


    old_stdout = sys.stdout
    sys.stdout = open(os.devnull, "w")
    try:
        id, data = reader.read()
    finally:
        sys.stdout.close()
        sys.stdout = old_stdout


    return (id, data)

def write(reader, data):
    reader.write(data)
    print("Written (data:"+ data + ")")

def get_id(data):
    print("get_id")
