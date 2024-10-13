from flask import Flask, make_response, render_template, Blueprint, request, redirect

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
            resp = make_response(redirect("/page"))
            print("login correct")
            #return redirect("/page")
            resp.set_cookie("loggedIn", "True")
            return resp
        else:
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