from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
from config.config import Config



app = Flask(__name__)
app.config['MONGO_URI']= Config.MONGO.MONGO_URI
app.config['SECRET_KEY'] = Config.MONGO.SECRET_KEY
mongo = PyMongo(app)


CORS(app)

db = mongo.db




