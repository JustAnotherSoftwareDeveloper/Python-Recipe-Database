from flask import Flask
from flask_mongoalchemy import MongoAlchemy
app = Flask(__name__)
app.config["DEBUG"] = True
app.config['MONGOALCHEMY_DATABASE'] = "recipes"
app.config["MONGOALCHEMY_SERVER"] = "172.17.0.2"
db = MongoAlchemy(app)

from app import routes