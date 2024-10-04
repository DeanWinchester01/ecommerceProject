from flask import Flask, render_template, Blueprint

loginBP = Blueprint("login",__name__)

@loginBP.route("/login", methods = ["POST","GET"])
def login():
    return render_template("login.html")