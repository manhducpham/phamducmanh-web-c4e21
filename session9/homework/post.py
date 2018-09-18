from mongoengine import Document, StringField

class Post(Document):
    name = StringField()
    email = StringField()
    your_id = StringField()
    password = StringField()
    