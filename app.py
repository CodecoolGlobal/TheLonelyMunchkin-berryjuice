from flask import Flask, render_template, url_for, request, redirect
from util import json_response

import queries, data_manager

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/game")
def game():
    dg_cards = queries.get_starting_dg_cards()
    tr_cards = queries.get_starting_tr_cards()
    gender = data_manager.get_gender_randomly()
    return render_template('game.html', dg_cards=dg_cards, tr_cards=tr_cards, gender=gender)

"""@app.route("/get-cards")
#@json_response
def get_dg_cards():
    dg_cards = queries.get_all_dg_cards()
    return redirect("/game")

@app.route("/get-cards")
#@json_response
def get_tr_cards():
    tr_cards = queries.get_all_tr_cards()
    return redirect("/game")"""

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )