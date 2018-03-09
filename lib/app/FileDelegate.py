from recipe import Recipe
import hashlib
import os

UPLOAD_FOLDER = os.getcwd() + "pdfs/"

class CreationModificationDelegate:


    def addNew(self,properties,file):
        hasher = hashlib.md5()
        buf=file.read()
        hasher.update(buf)
        new_name=hasher.hexdigest()+".pdf"
        file.save(os.path.join(UPLOAD_FOLDER,new_name))
        recipe=Recipe(title=properties["title"],filename=new_name,tags=properties["tags"],ingredients=properties["ingredients"])
        recipe.save()
        return recipe.toJson()


    def remove(self,properties):
        name=properties["filename"]
        recipe=Recipe.query.fileIs(filename=name).first()
        recipe.remove()
        return recipe.toJson()

    def edit(self,properties,file):
        if (file is not None and file.filename != ''):
            self.remove(properties)
            return self.addNew(properties,file)
        else:
            recipe = self.editMetaData(properties)
            return recipe.toJson()

    def editMetaData(self, properties):
        recipe = Recipe.query.fileIs(properties["filename"]).first()
        recipe.ingredients = properties["ingredients"]
        recipe.tags = properties["tags"]
        recipe.title = properties["title"]
        recipe.save()
        return recipe
