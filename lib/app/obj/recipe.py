import json

class Recipe:

    def __init__(self,title,filename,ingredients={},tags={}):
        self.title=title
        self.filename=filename
        self.ingredients=ingredients
        self.tags=tags

    def toJson(self):
        json.dumps(self.__dict__)
