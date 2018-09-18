import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds261072.mlab.com:61072/web2_serious_ex1

host = "ds261072.mlab.com"
port = 61072
db_name = "web2_serious_ex1"
user_name = "admin"
password = "CodeTheChange123456"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())