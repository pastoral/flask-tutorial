from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__, template_folder = 'templates')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/user/<name>")
def userprofile(name):
    return render_template("userprofile.html", name=name)


@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/process_login", methods=["POST"])
def processing_login():
    name = request.form["username"]
    return redirect(url_for("userprofile" , name = name))

@app.route("/home", methods = ["GET","POST"])
def home_page():
    if request.method=="GET":
        return render_template("home.html")
    elif request.method=="POST":
        return redirect(url_for('userprofile', name = request.form["username"]))


@app.route("/file_upload", methods = ["POST"])
def file_upload():
    file = request.file["filename"]
    if file.content_type == "text/plain":
        return file.read().decode()

    elif file.content_type == "application/vnd.ms-excel" or file.content_type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
        df = pd.read_excel(file)
        return df.to_html()


if __name__ == "__main__":
    app.run(debug=True)
