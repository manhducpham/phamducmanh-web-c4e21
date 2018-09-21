from mongoengine import Document, StringField, IntField #FloatField dùng cho số thực

class Post(Document):
    title = StringField()
    author = StringField()
    content = StringField()
    likes = IntField(default = 0)
    