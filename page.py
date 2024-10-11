from flask import Flask, Blueprint, render_template, request
from werkzeug.utils import secure_filename
import database
pageBP = Blueprint("page",__name__)

@pageBP.route("/page", methods = ["POST","GET"])
def page():
    #user = request.cookies.get("username")
    email = request.cookies.get("email")
    password = request.cookies.get("pass")

    print(email)
    print(password)

    data = database.GetVehicles()

    html = """"""
    for entry in range(len(data)):
        image = "/static/images/"+str(entry)+".png"
        html += "<button class = 'item'>"
        html += "<img class='itemImage' src='"
        html += image + "\'>"
        html += "</button>"
        
    #print(user)
    return render_template("page.html", dynamic_html = html)