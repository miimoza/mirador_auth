import json

def get_path(id):
    return "./database/{}.json".format(id)

def write_json(id, dict):
    path=get_path(id)
    json.dump(dict, open(path, 'w'))

def read_json(id):
    path=get_path(id)
    return json.loads(open(path).read())
