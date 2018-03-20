from app import app
import datetime
import os

from flask.json import jsonify
from flask import request
from flask import send_file
from app.FileDelegate import FileDelegate
from app.TagsDelegate import TagsDelegate
from app.IngredientsDelegate import IngredientsDelegate
from app.recipe import Recipe


@app.route('/', methods=['GET'])
@app.route('/status')
def index():
    response = {
        'status': "OK",
        'Time': datetime.datetime.now(),
        'project': 'recipes'
    }
    return jsonify(response)


@app.route('/search/byTags', methods=['GET'])
def searchByTags():
    tags = request.args['tags'].split(',')
    recipes = TagsDelegate().tagsInclude(tags)
    return jsonify(recipes)


@app.route('/search/byTags/all', methods=['GET'])
def searchByTagsAll():
    tags = request.args['tags'].split(',')
    recipes = TagsDelegate().tagsIncludeAll(tags)
    return jsonify(recipes)


@app.route("/search/all", methods=['GET'])
def getAll():
    recipes = Recipe.query.all()
    toJson = list(map((lambda r: r.toJson()), recipes))
    return jsonify(toJson)


@app.route("/search/ByIngredients", methods=['GET'])
def searchByIngredients():
    ingredients = request.args['ingredients'].split(',')
    recipes=IngredientsDelegate().ingredientsInclude(ingredients)
    return jsonify(recipes)

@app.route("/search/ByIngredients/all", methods=['GET'])
def searchByIngredientsAll():
    ingredients = request.args['ingredients'].split(',')
    recipes=IngredientsDelegate().ingredientsIncludeAll(ingredients)
    return jsonify(recipes)


@app.route("/recipes/put", methods=['POST'])
def addRecipe():
    delegate = FileDelegate()
    new_file = request.files['file']
    if new_file:
        json = delegate.addNew(
            file=request.files['file'], properties=request.args)
        return jsonify(json)
    return jsonify("{'error':'no file found'}")


@app.route("/recipes/edit", methods=['POST'])
def editRecipe():
    delegate = FileDelegate()
    json = delegate.edit(file=request.files['file'], properties=request.values)
    return jsonify(json)


@app.route("/recipes/remove", methods=['DELETE'])
def removeRecipe():
    delegate = FileDelegate()
    json = delegate.remove(
        file=request.files['file'], properties=request.values)
    return jsonify(json)


@app.route('/recipes/tags', methods=['GET'])
def getTags():
    tags = TagsDelegate().getTags()
    return jsonify(list(tags))


@app.route('/recipes/ingredients', methods=['GET'])
def getIngredients():
    ingredients = IngredientsDelegate().getIngredients()
    return jsonify(list(ingredients))

@app.route('/download',methods=['GET'])
def downloadFile():
    filename=request.args['filename']
    full_path=os.path.join(os.getcwd(),"pdfs",filename)
    return send_file(full_path)
    