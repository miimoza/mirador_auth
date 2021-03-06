from datetime import datetime, timedelta
import database
import os.path


def create(id):
    print("Create new User with ID: {}".format(str(id)))

    name = input("name: ").lower()
    if len(name) > 12:
        print("Less than 12 characters !!!")
        while len(name) > 12:
            name = input("name: ").lower()

    print("card {} was assigned to {}, welcome".format(id, name))

    dict = {
        "name": name,
        "nb_visit": 0,
        "last_visit": "0001-01-01 00:00:00.00",
        "grade": "visiteur"
    }
    database.write_json(id, dict)
    print("\nCorrectly saved in the database")
    return id

def id_exist(id):
    return os.path.isfile('./database/profiles/' + str(id) + '.json')

def get_info(id):
    return database.read_json(id)


def increment_visit(id, dict):
    now = datetime.now()
    last_visit = datetime.strptime(dict["last_visit"], "%Y-%m-%d %H:%M:%S.%f")

    if not now-timedelta(hours=24) <= last_visit <= now:
        print("Welcome")
        dict["last_visit"] = str(now)

        dict["nb_visit"] += 1

        if dict["grade"] != "propriétaire":
            if (dict["nb_visit"] >= 50):
                dict["grade"] = "platine"
                pass
            elif (dict["nb_visit"] >= 25):
                dict["grade"] = "or"
                pass
            elif (dict["nb_visit"] >= 10):
                dict["grade"] = "argent"
                pass
            elif (dict["nb_visit"] >= 5):
                dict["grade"] = "bronze"
                pass
            elif (dict["nb_visit"] >= 2):
                dict["grade"] = "cuivre"
                pass

        database.write_json(id, dict)
