import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds135519.mlab.com:35519/a-task-v2
#mongodb://<dbuser>:<dbpassword>@ds249718.mlab.com:49718/c4e21_manh
host = "ds249718.mlab.com"
port = 49718
db_name = "c4e21_manh"
user_name = "king_k0m4"
password = "CodeTheChange12babon"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())