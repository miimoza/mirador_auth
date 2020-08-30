import display
import os
import database

def dump():
    for i in range(3, 30):
        display.print_n(50, i, '|')
    display.print_n(51, 3, "------- RANKING BOARD -------")




    for filename in os.listdir('./database/'):
        print(filename)
