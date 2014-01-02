from app import database

class Post(database.Document):
    title = database.StringField(max_length=255, required=True)
    PL    = database.StringField(max_length=100, required=True)
    code  = database.StringField(required=True)
    ID    = database.StringField(max_length=100)

    meta = {
        'allow_inheritance': True
    }