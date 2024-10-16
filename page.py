import os
from flask import Flask, Blueprint, render_template, request
from werkzeug.utils import secure_filename
import database
import tempfile
import base64
import io
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
    saveFolder = "ecommerceProject/static/images/"
    for entry in range(len(data)):
        decoded = base64.b64decode(data[entry]["image"])
        imgStream = io.BytesIO(decoded)
        image = Image.open(imgStream)
        buffered = io.BytesIO()
        image.save(buffered,format="PNG")
        filepath = os.path.join(saveFolder,f"{entry}.png")
        
        with open(filepath,"wb") as fh:
            fh.write(decoded)
        
        items += "<button class='item'>"
        items += f"<img class='itemImage' src='static/images/"+str(entry)+".png'>"
        items += "</button>"

        #<form action="/logout" method="post">
        #</form>
    option1 = f"""
        <p class = 'sideoption' id = 'welcome'>' {username} '</p>
        <button class = sideoption id = "upload">Upload vehicle</button>
        <button class = "sideoption" id = "Logout">Log out</button>
    """
    option2 = """
        <button class = "sideoption" id = "login">Log in</button>
        <button class = "sideoption" id = "signup">Sign up</button>
    """
        
    if loggedIn == "True":
        return render_template("page.html", items = items, user_specifics = option1)
    return render_template("page.html", items = items, user_specifics = option2)
