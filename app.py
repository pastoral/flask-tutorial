from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder = 'templates')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/greet/<name>")
def greeting_user(name):
    return render_template("userprofile.html" , name = name)

@app.route('/add/<int:num1>/<int:num2>')
def add_numbers(num1,num2):
    return f'{num1} + {num2} = {num1+num2}'

@app.route("/handle_url_params") # http://127.0.0.1:5000/handle_url_params?title=Munir&name=Hoque
def handle_params():
    if "title" in request.args and "name" in request.args :
        return f'{request.args["title"]}  {request.args.get("name")}'
    else:
        return f'Something is missing'

@app.route("/test", methods=["GET","POST"])
def test_methods():
    if request.method=="GET":
        return f'<p> GET request trigerred </p>'
    elif request.method=="POST":
        return f'<p> POST request trigerred</p>'
    else:
        return f'You can not see me'



if __name__ == "__main__":
    app.run(debug=True)
