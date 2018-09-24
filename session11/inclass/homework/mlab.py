import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds211143.mlab.com:11143/web_3_homework

host = "ds211143.mlab.com"
port = 11143
db_name = 'web_3_homework'
username = 'admin'
password = 'CodeTheChange12babon'

def connect():
    mongoengine.connect(db_name, host = host, port = port, username = username, password = password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]

def item2json(item):
    import json
    return json.loads(item.to_json())