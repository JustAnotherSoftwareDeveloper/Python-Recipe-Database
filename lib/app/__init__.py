from flask import Flask
from flask_mongoengine import MongoEngine
app = Flask(__name__)
db=MongoEngine()
app.config["MONGODB_SETTINGS"] = {
    'db':'recipe-mongo',
    'host':'172.17.0.2',
    'port': 27017

}
from app import routes