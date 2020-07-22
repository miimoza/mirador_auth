import os
import time

def pretty_print(user_infos):
    print("MIRADOR AUTH V0.0.1")
    for k, v in user_infos:
        print(k)
        print(v)

def wait_and_clear():
    time.sleep(3)
    os.system('clear')
