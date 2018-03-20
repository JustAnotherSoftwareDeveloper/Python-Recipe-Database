from flask_mongoalchemy import BaseQuery

class Queries(BaseQuery):

    def ingredientsInclude(self,ingredients=[]):
        return self.filter({'ingredients':{'$in':ingredients}}).all()

    def ingredientsContainAll(self,ingredients=[]):
        return self.filter({'ingredients':{'$all':ingredients}}).all()

    def tagsInclude(self,tags=[]):
        return self.filter({'tags':{'$in':tags}}).all()

    def tagsIncludeAll(self,tags=[]):
        return  self.filter({'tags':{'$all':tags}}).all()

    def titleIsLike(self,match):
        return self.filter(match in self.type.title)

    def fileIs(self,filename):
        return self.filter(filename == self.type.filename)
