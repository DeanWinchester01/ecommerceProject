from flask import Flask, url_for, redirect, render_template, request, Blueprint,make_response
import database

signupBP = Blueprint("signup", __name__)
@signupBP.route("/signup", methods = ["POST","GET"])
def signup():
    return render_template("signup.html")

@signupBP.route("/signup/user", methods = ["POST","GET"])
def usersignup():
    if request.method != "POST":
        return redirect("/signup")
    
    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]
    confirmPass = request.form["confirmPass"]

    if not "@gmail.com" in email:
        print("wrong email format")
        return redirect("/signup")
    
    if password != confirmPass:
        print("missmatching passwords")
        return redirect("/signup")
    
    if not database.SignUp(username, email, password):
        print("email taken")
        return redirect('/signup')
    
    resp = make_response(redirect("/page"))
                
    resp.set_cookie("username", username)
    resp.set_cookie("email",email)
    resp.set_cookie("pass", password)
    resp.set_cookie("loggedIn", "True")

    return resp

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