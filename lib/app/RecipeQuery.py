from flask_mongoalchemy import BaseQuery

class Queries(BaseQuery):

    def ingredientsInclude(self=[]):
        return self.filter(any(i in self.type.ingredients for i in ingredients))

    def ingredientsContainAll(self,ingredients=[]):
        return self.filter(all(i in self.type.ingredients for i in ingredients))

    def tagsInclude(self,tags=[]):
        self.filter(any(tag in self.type.tags for tag in tags))

    def tagsIncludeAll(self,tags=[]):
        return  self.filter(all(tag in self.type.tags for tag in tags))

    def titleIsLike(self,match):
        return self.filter(match in self.type.title)

    def fileIs(self,filename):
        return self.filter(filename == self.type.filename)
