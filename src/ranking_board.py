import display
import os
import user

def dump():
    for i in range(3, 30):
        display.print_n(50, i, '|')
    display.print_n(51, 3, "------- RANKING BOARD -------")

    for id in os.listdir('./database/profiles'):
        userinfo = user.get_info(id)
        print(userinfo["name"] + ":" + userinfo["nb_visit"])
