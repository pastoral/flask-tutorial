from flask import Flask, render_template, request, redirect, url_for, Response, jsonify
import pandas as pd

app = Flask(__name__, template_folder = 'templates', static_folder='static', static_url_path = '/')

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login",methods=["GET", "POST"])
def userlogin():
    if request.method=="GET":
        return render_template("login.html")
    elif request.method=="POST":
        return redirect(url_for("dashboard", username=request.form["username"]))

@app.route('/dashboard')
def dashboard():
    name = request.args.get("username")
    return render_template('dashboard.html', username=name)


@app.route("/logout")
def logout():
    return redirect(url_for("userlogin"))

if __name__ == "__main__":
    app.run(debug=True)
