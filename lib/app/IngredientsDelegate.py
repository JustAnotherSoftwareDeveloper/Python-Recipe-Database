from app.recipe import Recipe
class IngredientsDelegate:

    def getIngredients(self):
        recipes=Recipe.query.all()
        ingredient_lists=map(lambda r: r.ingredients,recipes)
        return set([tag for ingredients in ingredient_lists for tag in ingredients])
    
    def ingredientsInclude(self,ingredients):
        recipes = Recipe.query.ingredientsInclude(ingredients=ingredients)
        if recipes is None:
            return []
        return list(map((lambda r: r.toJson()), recipes))
    
    def ingredientsIncludeAll(self,ingredients):
        recipes = Recipe.query.ingredientsContainAll(ingredients=ingredients)
        if recipes is None:
            return []
        return list(map((lambda r: r.toJson()), recipes))