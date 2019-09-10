from flask import Flask, render_template, url_for, request, redirect
#from util import json_response

import queries

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/game")
def game():
    return render_template("game.html")

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )