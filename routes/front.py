from flask import Blueprint, app, redirect, render_template, request
import connection

front = Blueprint("front", __name__, static_folder="static", template_folder="templates/front")

@front.route('/')
@front.route('/home')
def home():
    return render_template("front/home.html")

@front.route('/fleet')
def fleet():
    res = connection.fetch_all_airframes()
    airframes_dict = []
    for row in res:
        row_as_dict = row._mapping
        airframes_dict.append(row_as_dict)
    fleet = set(airframes_dict)
    return render_template("front/fleet.html")