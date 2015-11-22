from flask import Flask
from flask import render_template, url_for, request
import requests
import json

import pymongo
from pymongo import MongoClient
client = MongoClient()
db = client.local
people = db.people

app = Flask(__name__)
app.config["DEBUG"] = True

PROPS = ['name','grade','sex','motivation','behavior','participation','postivies','negatives']

@app.route("/makeclass/<int:num_students>", methods=['GET', 'POST'])
def make_form(num_students):
    if request.method == "GET":
        return render_template('entry.html',num = num_students,props=PROPS)
    if request.method == "POST":
        data = request.form
        print data
        return render_template('success.html')





















if __name__ == "__main__":
    app.run()
