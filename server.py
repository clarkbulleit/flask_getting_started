from flask import Flask, jsonify, request
import math
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
    dist = math.sqrt((r["a"][0] - r["b"][0]) ^ 2 + ((r["a"][1] - r["b"][1]) ^ 2))
    r["distance"] = round(dist, 2)

    return jsonify(r), 200


if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=5000)
    app.run(host="127.0.0.1", port=5001)
