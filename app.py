from flask import Flask, render_template, request, redirect, url_for, Response, jsonify, session, make_response


app = Flask(__name__, template_folder = 'templates', static_folder='static', static_url_path = '/')

# REQUIRED for session
app.secret_key = "MYSECRETKEY"

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login",methods=["GET", "POST"])
def userlogin():
    if request.method=="GET":
        return render_template("login.html")
    elif request.method=="POST":
        #return redirect(url_for("dashboard", username=request.form["username"])) ##
        username = request.form["username"]
        # Save user in session ####
        session["user"] = username
        
        # Save user data in Cookies ####
        ## create the redirect response, set cookies on that response, and then return the response at the end ###
        resp = make_response(redirect(url_for("dashboard")))
        
        resp.set_cookie("lang_pref", "Spanish")
        resp.set_cookie("theme_color", "Dark")
        
        # return redirect(url_for("dashboard")) ##
        return resp

@app.route('/dashboard')
def dashboard():
    #name = request.args.get("username") ##
    #return render_template('dashboard.html', username=name) ##
    ### GET the User data from the Session ###
    if "user" in session:
        name = session["user"]
        
        ## Get the Cookie Data ##
        lang_pref = request.cookies["lang_pref"]
        theme_color = request.cookies["theme_color"]
        ## Below two lines ensure accessing the Dashboard only if the user is logged in ##
        return render_template(
            'dashboard.html', 
            username=name,
            lang_pref = lang_pref,
            theme_color = theme_color
            ) 
    return redirect(url_for("userlogin"))


@app.route("/logout")
def logout():
    #Logout removes session: ##
    session.pop("user", None)
    return redirect(url_for("userlogin"))

if __name__ == "__main__":
    app.run(debug=True)
