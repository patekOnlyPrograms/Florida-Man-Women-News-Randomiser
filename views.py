import json

from flask import Blueprint, render_template, jsonify

views = Blueprint(__name__,"views")

@views.route('/')
def home():
    with open('static/data.json') as f:
        names = json.load(f)
    return render_template("index.html", names_json=jsonify(names).json)


@views.route("/about")
def about():
    return render_template("about.html")