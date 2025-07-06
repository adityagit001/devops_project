from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api")
def lwinfo():
    return "i m lw from India"

@app.route("/phone")
def phone():
    return "1234567890"

app.run(host="0.0.0.0")