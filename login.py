from flask import Flask, render_template, Blueprint, request, redirect

loginBP = Blueprint("login",__name__)

@loginBP.route("/login", methods = ["POST","GET"])
def login():
    if request.method == "POST":
        print("log in")
        email = request.form["email"]
        password = request.form["password"]
        print(email, password)

        savedemail = request.cookies.get("email")
        savedpassword = request.cookies.get("pass")

        print(savedemail)
        print(savedpassword)
        #print(savedEmail, savedPass)

        if email == savedemail and password == savedpassword:
            print("login correct")
            return redirect("/page")
        else:
            print("login incorrect")
            return render_template("login.html")
    else:
        return render_template("login.html")
            

    #password = request.cookies.get("pass")