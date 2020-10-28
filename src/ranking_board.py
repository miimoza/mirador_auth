import display
import os
import user
from operator import itemgetter

def dump():
    for i in range(3, 30):
        display.print_n(50, i, '|')



    display.print_n(0, 29, "   2:Cuivre 5:Bronze 10:Argent 25:Or 50:Platine")
    display.print_n(51, 3, "------- RANKING BOARD -------")





    userinfo_list = []
    for id in os.listdir('./database/profiles'):
        userinfo = user.get_info(os.path.splitext(id)[0])
        userinfo_list.append(userinfo)

    ranking_board = sorted(userinfo_list, key=itemgetter('nb_visit'), reverse=True)

    line = 4
    for userinfo in ranking_board:
        if userinfo["grade"] == "or":
            color = "\e[93m"
        else
            color = "\e[39m"

        color_default = "\e[39m"
        display.print_n(51, line, color + userinfo["name"].ljust(13) + userinfo["grade"].ljust(13) + str(userinfo["nb_visit"]).rjust(3) + color_default)
        line += 1
