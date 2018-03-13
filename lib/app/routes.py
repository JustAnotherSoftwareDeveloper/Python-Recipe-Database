from app import app
import datetime

from flask.json import jsonify
from flask import request
from app.FileDelegate import FileDelegate
from app.recipe import Recipe


@app.route('/', methods=['GET'])
@app.route('/status')
def index():
    response = {'status': "OK", 'Time': datetime.datetime.now(),
                                                              'project': 'recipes'}
    return jsonify(response)


@app.route('/search/byTags', methods=['GET'])
def searchByTags():
    return jsonify("{}")


@app.route('/search/byTags/all', methods=['GET'])
def searchByTagsAll():
    return jsonify("{}")


@app.route("/search/all", methods=['GET'])
def getAll():
    recipes = Recipe.query.all()
    toJson = list(map((lambda r: r.toJson()), recipes))
    return jsonify(toJson)



@app.route("/search/ByIngredients", methods=['GET'])
def searchByIngredients():
    return jsonify("{}")


@app.route("/search/ByIngredients/all", methods=['GET'])
def searchByIngredientsAll():
    return jsonify("{}")


@app.route("/recipes/put", methods=['POST'])
def addRecipe():
    delegate=FileDelegate()
    new_file=request.files['file']
    if new_file:
        json=delegate.addNew(file=request.files['file'],properties=request.args)
        return jsonify(json)
    return jsonify("{'error':'no file found'}")


@app.route("/recipes/edit", methods=['POST'])
def editRecipe():
    delegate=FileDelegate()
    json=delegate.edit(file=request.files['file'],properties=request.values)
    return jsonify(json)

@app.route("/recipes/remove",methods=['DELETE'])
def removeRecipe():
    delegate=FileDelegate()
    json=delegate.remove(file=request.files['file'],properties=request.values)
    return jsonify(json)

@app.route('/recipes/tags', methods=['GET'])
def getTags():
    return jsonify("{}")


@app.route('/recipes/ingredients', methods=['GET'])
def getIngredients():
    return jsonify("{}")
