from flask import Flask, make_response, render_template, Blueprint, request, redirect
from database import LogIn

loginBP = Blueprint("login",__name__)

@loginBP.route("/login", methods = ["POST","GET"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
                
        login = LogIn(email, password)
        if login != False:
            resp = make_response(redirect("/page"))
            resp.set_cookie("email",login["email"])
            resp.set_cookie("username",login["username"])
            resp.set_cookie("loggedIn", "True")
            return resp
        
        print("login incorrect")
        return render_template("login.html")
    else:
        if request.cookies.get("loggedIn") == "True":
            return redirect("/page")
        
        return render_template("login.html")
            
@loginBP.route("/logout", methods = ["POST","GET"])
def logout():
    resp = make_response(redirect("/login"))
    resp.set_cookie("loggedIn","False")
    resp.delete_cookie("email")
    resp.delete_cookie("pass")
    resp.delete_cookie("username")

    return resp
    #password = request.cookies.get("pass")