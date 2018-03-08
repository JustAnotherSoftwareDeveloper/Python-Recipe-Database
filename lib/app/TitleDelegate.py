from recipe import Recipe


class UploadDelegate:
    def getRecipesByTitle(self, title):
        recipes = Recipe.query.titleIsLike(title)
        toJson = list(map(lambda r: r.toJson()), recipes)
        return toJson
