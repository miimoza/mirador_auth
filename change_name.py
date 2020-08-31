#!/usr/bin/env python3
from src import database

def main():
    with open("./database/logs/profiles_creation.log", "r") as log:
        last_creations = log.readlines()[-5]

    for l in last_creations.splitlines():
        print('[0] : ' +  l)

    while len(name) > 12:
        name=input("name: ").lower()

    dict = database.read_json(id)
    dict["name"] = name
    database.write_json(id, dict)

    print("card {} was assigned to {}, welcome".format(id, dict["name"]))

if __name__ == "__main__":
    main()
