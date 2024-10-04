from flask import Flask, Blueprint, render_template

pageBP = Blueprint("page",__name__)

@pageBP.route("/page", methods = ["POST","GET"])
def page():
    return render_template("page.html")