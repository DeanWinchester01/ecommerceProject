from flask import Flask, Blueprint, render_template, request

pageBP = Blueprint("page",__name__)

@pageBP.route("/page", methods = ["POST","GET"])
def page():
    user = request.cookies.get("username")
    email = request.cookies.get("email")
    password = request.cookies.get("pass")

    print(user)
    print(email)
    print(password)

    return render_template("page.html")