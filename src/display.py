import os
import time

def print_banner():
    print("*"*36)
    print("* MIRADOR MEMBER CARD AUTHENTIFIER *")
    print("*"*36)
    print("") 


def print_userinfo(user_infos):
    if user_infos["nb_visit"] == 1:
        print("BIENVENUE {}".format(user_infos["name"].upper()))
    else:
        print("BONJOUR {}".format(user_infos["name"].upper()))
    print()
    for k in user_infos:
        print("{}: {}".format(str(k).capitalize(), str(user_infos[k]).capitalize()))

def wait_and_clear():
    print("")
    print("*"*36)
    for i in range(0,36):
        print(".",end='', flush=True)
        time.sleep(0.2)
    os.system('clear')
