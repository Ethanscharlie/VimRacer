import flask as fl
import os

SAMPLE_INPUT = "Example body, of text"
SAMPLE_OUTPUT = "Example, of text body!"

app = fl.Flask(__name__)


@app.route("/")
def main():
    return fl.render_template("index.html")


@app.route("/get-level")
def getLevel():
    return f'{{"in": "{SAMPLE_INPUT}", "out": "{SAMPLE_OUTPUT}"}}'


@app.route("/check-strokes")
def checkStrokes():
    strokes = fl.request.args.get("strokes")
    print(f"Strokes: {strokes}")
    return "Wrong!"
