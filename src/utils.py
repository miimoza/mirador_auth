# UTILS

def log(filename, line):
    with open("./database/logs/" + filename, 'a+') as file:
        file.write(line + '\n')
