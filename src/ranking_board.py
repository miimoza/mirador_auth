import display
import os
import user
from operator import itemgetter

def dump():
    for i in range(3, 30):
        display.print_n(50, i, '|')



    display.print_n(0, 29, "   \033[31m2:Cuivre \033[33m5:Bronze \033[97m10:Argent \033[93m25:Or \033[96m50:Platine\033[0m")
    display.print_n(51, 3, "------- RANKING BOARD -------")





    userinfo_list = []
    for id in os.listdir('./database/profiles'):
        userinfo = user.get_info(os.path.splitext(id)[0])
        userinfo_list.append(userinfo)

    ranking_board = sorted(userinfo_list, key=itemgetter('nb_visit'), reverse=True)

    line = 4
    for userinfo in ranking_board:
        switcher = {
            "cuivre": "\033[31m",
            "bronze": "\033[33m",
            "argent": "\033[97m",
            "or": "\033[93m",
            "platine": "\033[96m"
        }

        color = switcher.get(userinfo["grade"], "\033[0m")

        display.print_n(51, line, color + userinfo["name"].ljust(13) + userinfo["grade"].ljust(13) + str(userinfo["nb_visit"]).rjust(3) + "\033[0m")
        line += 1
