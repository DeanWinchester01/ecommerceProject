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

    items = """
    <div class="filterview" id="filterview">
        <div class="option">
            <label>Price range</label>
            <div>
                <input type="radio" id="price1" name="price">
                <label for="price1">$5,001 - $10,000</label>
            </div>
            <div>
                <input type="radio" id="price2" name="price">
                <label for="price2">$10,001 - $20,000</label>
            </div>
        </div>

        <div class="sideoption">
            <input type="checkbox" id="cylinder">
            <label for="cylinder">4 cylinder</label>
        </div>
        <div class="sideoption">
            <input type="checkbox" id="speed">
            <label for="speed">200km top speed</label>
        </div>
        <div class="sideoption">
            <input type="checkbox" id="medium">
            <label for="medium">4 seater</label>
        </div>
        <div class="sideoption">
            <input type="checkbox" id="chrissy">
            <label for="chrissy">chrissy</label>
        </div>"""
    
        
        #items += "<button class='item' id = '"+str(id)+"'>"
        #items += f"<img class='itemImage' src='static/images/"+str(id)+".png'>"
        #items += "</button>"

        #<form action="/logout" method="post">
        #</form>
    option1 = f"""
        <p class = 'sideoption' id = 'welcome'>' {username} '</p>
        <button class = sideoption id = "upload">Upload vehicle</button>
        <button class = sideoption id = "uploads">My vehicles</button>
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
        data = GetData("public")
        return render_template("page.html", dynamic = data, user_specifics = option1, searchoptions = items)
    return render_template("page.html", dynamic = data, user_specifics = option2)

@pageBP.route("/page/<user>")
def userpage(user):
    loggedIn = request.cookies.get("loggedIn")
    username = request.cookies.get("username")
    
    if loggedIn == "True" and username == user:
        email = request.cookies.get("email")
        data = GetData(email)
        print(data)
        return render_template("userpage.html", dynamic = data)
    return render_template("error.html")


#@pageBP.route("/page/getdata/<data>", methods = ["POST","GET"])
def GetData(data):
    saveFolder = "ecommerceProject/static/images/"
    vehicles = database.GetVehicles(data)
    for entry in range(len(vehicles)):
        decoded = base64.b64decode(vehicles[entry]["image"])
        imgStream = io.BytesIO(decoded)
        image = Image.open(imgStream)
        buffered = io.BytesIO()
        image.save(buffered,format="PNG")
        id = vehicles[entry]["_id"]
        filepath = os.path.join(saveFolder,f"{id}.png")
        
        with open(filepath,"wb") as fh:
            fh.write(decoded)

    newData = []
    for entry in vehicles:
        entry["_id"] = str(entry["_id"])
        newData.append(entry)
        
    return newData
