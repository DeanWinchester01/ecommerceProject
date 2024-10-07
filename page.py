from flask import Flask, Blueprint, render_template, request
from werkzeug.utils import secure_filename
pageBP = Blueprint("page",__name__)

@pageBP.route("/page", methods = ["POST","GET"])
def page():
    #user = request.cookies.get("username")
    email = request.cookies.get("email")
    password = request.cookies.get("pass")

    print(email)
    print(password)
    #print(user)
    return render_template("page.html")

@pageBP.route("/page/upload", methods = ["GET","POST"])
def upload():
    print("upload")
    file = request.files["file"]
    file.save(secure_filename(file.filename))
    print(file)

    return "Upload sucessfull"