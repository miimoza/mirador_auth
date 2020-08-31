#!/usr/bin/env python3
from src import database

def main():
    last_creations=[]
    with open("./database/logs/profiles_creation.log", "r") as log:
        for line in (log.readlines() [-5:]):
            last_creations.append(line)

    for i in range(0, len(last_creations)):
        print("[" + str(i) + "] " + last_creations[i], end='')

    i = input("number: ")
    id = last_creations[int(i)].split(',')[0]
    print("id:" + id)

    name = input("name: ").lower()
    if len(name) > 12:
        print("Less than 12 characters !!!")
        while len(name) > 12:
            name = input("name: ").lower()



    dict = database.read_json(id)
    dict["name"] = name
    database.write_json(id, dict)

    print("card {} was assigned to {}, welcome".format(id, dict["name"]))

if __name__ == "__main__":
    main()
