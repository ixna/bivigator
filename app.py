import flask

app = flask.Flask(__name__)

@app.route("/", methods=["GET"])
def main():
    return "Hello World"

app.run("0.0.0.0")
