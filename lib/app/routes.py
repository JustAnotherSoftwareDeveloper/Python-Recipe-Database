from app import app
import datetime

from flask.json import jsonify
from flask import request

@app.route('/',methods=['GET'])
@app.route('/status')
def index():
    response = {'status':"OK",'Time':datetime.datetime.now(),'project':'recipes'}
    return jsonify(response)

@app.route('/search/byTags',methods=['GET'])
def searchByTags():
    return jsonify("{}")

@app.route("/search/all",methods=['GET'])
def getAll():
    return jsonify("{}")

@app.route("/search/ingredients",methods=['GET'])
def searchByIngredients():
    return jsonify("{}")

@app.route("/recipes/put",methods=['PUT'])
def addRecipe():
    return jsonify("{}")

@app.route("/recipes/edit",methods=['POST'])
def editRecipe():
    return jsonify("{}")

@app.route('/recipes/tags',methods=['GET'])
def getTags():
    return jsonify("{}")

@app.route('/recipes/ingredients',methods=['GET'])
def getIngredients():
    return jsonify("{}")

