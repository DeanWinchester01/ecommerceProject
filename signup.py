from flask import Flask, url_for, redirect, render_template, request, Blueprint,make_response

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
                resp = make_response(redirect("/page"))
                
                resp.set_cookie("username", username)
                resp.set_cookie("email",email)
                resp.set_cookie("pass", password)
                return resp

            else:
                print("missmatching passwords")
        else:
            print("wrong email format")

@signupBP.route("/signup/login")
def login():
    return redirect("/login")



#@app.route("/page", methods = ["GET","POST"])
#def page():
    #user = (request.method == 'POST') and request.form['nm'] or request.args.get('nm')
 #   return render_template("page.html")

#@app.route("/login", methods = ["GET","POST"])
#def login():
 #   return render_template("login.html")