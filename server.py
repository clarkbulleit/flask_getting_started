from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route("/name", methods=["GET"])
def name():
    return "hello, Clark Bulleit"


@app.route("/hello/<name>", methods=["GET"])
def hello(name):
    d = {
        "message": "Hello there, {}".format(name)
    }

    return jsonify(d)

@app.route("/distance", methods=["POST"])
def distance():
    r = request.get_json()
    

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001)
