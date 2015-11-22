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

@app.route("/makeclass/<int:num_students>")
def make_form(num_students):
    return render_template('entry.html',num = num_students)





















if __name__ == "__main__":
    app.run()