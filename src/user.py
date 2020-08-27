from datetime import datetime, timedelta
import database

def create(id):
    print("Create new User with ID: {}".format(str(id)))
    dict = {
        "name": "Julien",
        "nb_visit": 0,
        "last_visit": "0001-01-01 00:00:00.00",
        "grade": "visiteur"
    }
    database.write_json(id, dict)
    print("\nYou can ask the administrator")
    print("to get another name than 'Julien'")
    return id

def get_info(id):
    return database.read_json(id)

def increment_visit(id, dict):
    print(now)
    now = datetime.now()
    last_visit = datetime.strptime(dict["last_visit"], "%Y-%m-%d %H:%M:%S.%f")

    print("now: " + str(now))
    print("last visit:", str(last_visit))
    print(now-timedelta(hours=24) <= last_visit <= now)

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
