import json

def create():
    id = 0
    print("Create new User with ID: {}".format(str(id)))
    return id

def get_info(id):
    path="./database/{}.json".format(id)
    return json.loads(open(path).read())

def increment_visit(id):
    print("increment_user_visit")
