from flask import Flask, url_for, redirect, render_template, request, Blueprint

signupBP = Blueprint("signup", __name__)
@signupBP.route("/signup", methods = ["POST","GET"])
def signup():
    return render_template("signup.html")

@signupBP.route("/signup/user", methods = ["POST","GET"])
def usersignup():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        confirmPass = request.form["confirmPass"]

        if "@gmail.com" in email:
            if password == confirmPass:
                return render_template("page.html")
            else:
                print("missmatching passwords")
        else:
            print("wrong email format")


#@app.route("/page", methods = ["GET","POST"])
#def page():
    #user = (request.method == 'POST') and request.form['nm'] or request.args.get('nm')
 #   return render_template("page.html")

#@app.route("/login", methods = ["GET","POST"])
#def login():
 #   return render_template("login.html")