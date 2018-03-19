from app.recipe import Recipe
class TagsDelegate:

    def getTags(self):
        recipes=Recipe.query.all()
        tag_lists=map(lambda r: r.tags,recipes)
        return set([tag for tags in tag_lists for tag in tags])
    
    def tagsInclude(self,tags):
        recipes = Recipe.query.tagsInclude(tags=tags)
        if recipes is None:
            return []
        return list(map((lambda r: r.toJson()), recipes))