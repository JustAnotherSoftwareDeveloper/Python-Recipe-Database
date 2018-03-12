import json
from app.RecipeQuery import Queries
from app import db


class Recipe(db.Document):
    query_class=Queries
    title = db.StringField()
    filename=db.StringField()
    ingredients=db.ListField(db.StringField())
    tags=db.ListField(db.StringField())

    def toJson(self):
        json={}
        json['title']=self.title
        json['filename']=self.filename
        json['ingredients']=self.ingredients
        json['tags']=self.tags
        return json


