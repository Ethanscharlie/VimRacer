from flask import Flask, render_template
import os

SAMPLE_INPUT = "Example body, of text"
SAMPLE_OUTPUT = "Example, of text body!"

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/get-level")
def getLevel():
    return f'{{"in": "{SAMPLE_INPUT}", "out": "{SAMPLE_OUTPUT}"}}'
