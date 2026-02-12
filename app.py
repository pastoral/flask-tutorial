from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder = 'templates')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/user/<name>")
def userprofile(name):
    return render_template("userprofile.html", name=name)


@app.route("/login", methods=['GET'])
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


if __name__ == "__main__":
    app.run(debug=True)
