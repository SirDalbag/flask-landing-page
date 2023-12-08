from flask import render_template
from app import app
import json


@app.route("/")
def index():
    with open("app\plans.json") as file:
        data = json.load(file)
    return render_template("index.html", plans=data)
