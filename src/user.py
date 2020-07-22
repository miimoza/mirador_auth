import json
import database

def create():
    id = 0
    print("Create new User with ID: {}".format(str(id)))
    dict = {
        "user":" Julien",
        "nb_visit": 1
    }
    database.write_json(id, dict)
    return id

def get_info(id):
    return database.read_json(id)

def increment_visit(id, dict):
    dict["nb_visit"] += 1
    database.write_json(id, dict)
