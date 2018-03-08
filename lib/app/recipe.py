import json
from RecipeQuery import Queries
from app import db


class Recipe(db.Document):
    query_class=Queries
    title = db.StringField()
    filename=db.StringField()
    ingredients=db.ListField(db.StringField())
    tags=db.ListField(db.StringField)

    def toJson(self):
        json.dumps(self.__dict__)


