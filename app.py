from flask import Flask, render_template, request, redirect, url_for, Response, jsonify
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

@app.route("/convert_csv", methods=["POST"])
def convert_csv():
    file = request.files["filename"]
    df = pd.read_excel(file)
    response = Response(
        df.to_csv(),
        mimetype = 'text/csv',
        headers = {
            'Content-Disposition': 'attachment; filename=result.csv'
        }
    )
    return response
    

@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()  # Get JSON data from frontend
    first_name = data.get("first_name")
    last_name = data.get("last_name")

    message = f'Hello {first_name} {last_name},  Welocome to Jason'
    return jsonify({"response_message": message})



if __name__ == "__main__":
    app.run(debug=True)
