import database

def create(id):
    print("Create new User with ID: {}".format(str(id)))
    dict = {
        "name": "Julien",
        "nb_visit": 0,
        "grade": "visiteur"
    }
    database.write_json(id, dict)
    print("\nYou can ask the administrator")
    print("to get another name than 'Julien'")
    return id

def get_info(id):
    return database.read_json(id)
        

    return userinfo

def increment_visit(id, dict):
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
