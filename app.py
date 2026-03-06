from flask import Flask, render_template, request, redirect, url_for, Response, jsonify
import pandas as pd

app = Flask(__name__, template_folder = 'templates', static_folder='static', static_url_path = '/')

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
