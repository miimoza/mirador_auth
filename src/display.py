import os
import time

def print_banner():
    print("="*80)
    print("*********************** MOULIN  MEMBER CARD AUTHENTIFIER ***********************")
    print("="*80)
    print("")
    move_cursor(30, 0)
    print("="*80)


def print_userinfo(user_infos):
    if user_infos["nb_visit"] == 1:
        print("BIENVENUE {}".format(user_infos["name"].upper()))
    else:
        print("BONJOUR {}".format(user_infos["name"].upper()))
    print()
    for k in user_infos:
        print("{}: {}".format(str(k).capitalize(), str(user_infos[k]).capitalize()))




def wait_and_clear():
    move_cursor(31, 0)
    for i in range(0,80):
        print(".",end='', flush=True)
        time.sleep(0.1)
    os.system('clear')

def move_cursor(y, x):
	os.system("tput cup " + str(y) + " " + str(x))

def print_n(w, n, s):
	move_cursor(n, w)
	print(s)

	return n+1
