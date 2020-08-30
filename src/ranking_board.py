import display
import os
import user
from operator import itemgetter

def dump():
    for i in range(3, 30):
        display.print_n(50, i, '|')
    display.print_n(51, 3, "------- RANKING BOARD -------")





    userinfo_list = []
    for id in os.listdir('./database/profiles'):
        userinfo = user.get_info(os.path.splitext(id)[0])

        userinfo_list.append({userinfo["name"], userinfo["grade"], userinfo["nb_visit"]})

    ranking_board = sorted(userinfo_list, key=itemgetter('nb_visit'))

    for userinfo in ranking_board:
        display.print_n(51, line, userinfo["name"] + ": " + userinfo["grade"] + '(' + str(userinfo["nb_visit"]) + ')')
        line += 1
