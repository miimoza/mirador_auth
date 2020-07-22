import os
import time

def pretty_print(user_infos):
    print("****************")
    print("* MIRADOR AUTH *")
    print("****************")
    print()
    if user_infos["nb_visit"] == 1:
        print("BIENVENUE {}".format(user_infos["name"].upper()))
    else:
        print("BONJOUR {}".format(user_infos["name"].upper()))
    print()
    for k in user_infos:
        print("{}: {}".format(str(k).capitalize(), str(user_infos[k]).capitalize()))

def wait_and_clear():
    time.sleep(1)
    print("================")
    #os.system('clear')
