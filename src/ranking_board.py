import display
import os
import user

def dump():
    for i in range(3, 30):
        display.print_n(50, i, '|')
    display.print_n(51, 3, "------- RANKING BOARD -------")





    ranking_board = []
    for id in os.listdir('./database/profiles'):
        userinfo = user.get_info(os.path.splitext(id)[0])

        ranking_board.append({userinfo["name"], userinfo["grade"], userinfo["nb_visit"]})

    line = 4
    for userinfo in ranking_board:

        display.print_n(51, line, userinfo["name"] + ": " + userinfo["grade"] + '(' + str(userinfo["nb_visit"]) + ')')
        line += 1

    for k in user_infos:
