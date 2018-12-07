import socket
import json
import os.path
from flask import Flask, request, make_response, jsonify

app = Flask(__name__)

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "database.json")

with open(path, "r") as f:
    wines = json.load(f)


@app.route('/', methods=['GET'])
def get_root():
    return "EXAMPLE: curl http://127.0.0.1:5000/wine/1"


@app.route('/wine/<int:wine_id>', methods=['GET'])
def get_wine(wine_id):
    wine = [wine for wine in wines if wine['id'] == wine_id]
    if len(wine) == 0:
        abort(404)
    return jsonify({'wine': wine[0]})


@app.route("/hostname")
def return_hostname():
    """Returns the hostname"""
    return"This app is served from {} to {}".format(socket.gethostname(), request.remote_addr)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
