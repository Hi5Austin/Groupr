from flask import Flask
from flask import render_template, url_for
import requests
import json

import pymongo
from pymongo import MongoClient
client = MongoClient()
db = client.local
people = db.people

app = Flask(__name__)
app.config["DEBUG"] = True























if __name__ == "__main__":
    app.run()g
