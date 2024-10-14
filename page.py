from flask import Flask, Blueprint, render_template, request
from werkzeug.utils import secure_filename
import database
import io
import base64
import zlib
from PIL import Image
pageBP = Blueprint("page",__name__)

@pageBP.route("/page", methods = ["POST","GET"])
def page():
    #user = request.cookies.get("username")
    email = request.cookies.get("email")
    password = request.cookies.get("pass")
    loggedIn = request.cookies.get("loggedIn")
    print(loggedIn)
    username = request.cookies.get("username")
    print("logged in")
    print(email)
    print(password)

    data = database.GetVehicles()

    items = """"""
    cmap = {'0': (255,255,255),
        '1': (0,0,0)}
    for entry in range(len(data)):
        print(data[entry]["image"])
        decoded = base64.b64decode(data[entry]["image"])
        #uncompressed = zlib.decompress(decoded)
        img.putdata(data)
        img.show() 
        #file = io.BytesIO(base64.decode(entry["image"]))
        file = "/static/images/"+str(entry)+".png"
        items += "<button class = 'item'>"
        items += f"<img class='itemImage' src='"
        items += file + "\'>"
        items += "</button>"

    option1 = f"""
        <p class = 'sideoption' id = 'welcome'>' {username} '</p>
        <button class = sideoption id = "upload">Upload vehicle</button>
        <form action="/logout" method="post">
        <button class = "sideoption" id = "Logout">Log out</button>
        </form>
    """
    option2 = """
        <button class = "sideoption" id = "login">Log in</button>
        <button class = "sideoption" id = "signup">Sign up</button>
    """
        
    if loggedIn == "True":
        return render_template("page.html", items = items, user_specifics = option1)
    return render_template("page.html", items = items, user_specifics = option2)
