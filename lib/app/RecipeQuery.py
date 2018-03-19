from flask_mongoalchemy import BaseQuery

class Queries(BaseQuery):

    def ingredientsInclude(self,ingredients=[]):
        return self.filter(any(i in self.type.ingredients for i in ingredients))

    def ingredientsContainAll(self,ingredients=[]):
        return self.filter(all(i in self.type.ingredients for i in ingredients))

    def tagsInclude(self,tags=[]):
        return self.filter({'tags':{'$in':tags}}).all()

    def tagsIncludeAll(self,tags=[]):
        return  self.filter({'tags':{'$in':tags}}).all()

    def titleIsLike(self,match):
        return self.filter(match in self.type.title)

    def fileIs(self,filename):
        return self.filter(filename == self.type.filename)
