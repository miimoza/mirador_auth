def create():
    id = 84
    print("Create new User with ID " + str(id))
    return id

def get_info(id):
    print("get_user_info")
    return {"user":"Julien", "nb_visit":17}

def increment_visit(id):
    print("increment_user_visit")
