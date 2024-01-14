from peewee import *

db = SqliteDatabase('data/information.db')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    username = CharField(unique=True)

def initialize_db():
    db.connect()
    db.create_tables([User], safe=True)