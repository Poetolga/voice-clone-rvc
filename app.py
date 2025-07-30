import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "RVC Voice Clone ready"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
