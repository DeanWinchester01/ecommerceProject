import os
from flask import Flask, Blueprint, render_template, request, jsonify
from werkzeug.utils import secure_filename
import database
import tempfile
import base64
import io
from PIL import Image
pageBP = Blueprint("page",__name__)

@pageBP.route("/page", methods = ["POST","GET"])
def page():
    loggedIn = request.cookies.get("loggedIn")
    username = request.cookies.get("username")

    #data = database.GetVehicles()

    items = """"""
    
        
        #items += "<button class='item' id = '"+str(id)+"'>"
        #items += f"<img class='itemImage' src='static/images/"+str(id)+".png'>"
        #items += "</button>"

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
        
    #if loggedIn == "True":
        #return render_template("page.html", items = items, user_specifics = option1)
    #return render_template("page.html", items = items, user_specifics = option2)
    if loggedIn == "True":
        return render_template("page.html", user_specifics = option1)
    return render_template("page.html", user_specifics = option2)

@pageBP.route("/page/getdata", methods = ["POST","GET"])
def GetData():
    saveFolder = "ecommerceProject/static/images/"
    data = database.GetVehicles()
    for entry in range(len(data)):
        decoded = base64.b64decode(data[entry]["image"])
        imgStream = io.BytesIO(decoded)
        image = Image.open(imgStream)
        buffered = io.BytesIO()
        image.save(buffered,format="PNG")
        id = data[entry]["_id"]
        filepath = os.path.join(saveFolder,f"{id}.png")
        
        with open(filepath,"wb") as fh:
            fh.write(decoded)

    newData = []

    for entry in data:
        entry["_id"] = str(entry["_id"])
        newData.append(entry)

    return jsonify(newData)