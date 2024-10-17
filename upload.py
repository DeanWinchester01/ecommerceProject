import os
from flask import Flask, Blueprint, render_template, request, redirect
from werkzeug.utils import secure_filename
import database
import io
import base64
from PIL import Image

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "flaskenv/ecommerceProject/static/images/"

uploadBP = Blueprint("upload",__name__)

@uploadBP.route("/upload", methods = ["GET","POST"])
def UploadVehicle():
    return render_template("upload.html")

@uploadBP.route("/upload/vehicle", methods = ["GET","POST"])
def GetVehicleImage():
    if request.method == "POST":
        file = request.files["image"]
        file.save(secure_filename(file.filename))
        b64string = ""
        with Image.open(file.filename) as img:
            buffered = io.BytesIO()
            img.save(buffered, format="PNG")
            binary = buffered.getvalue()
            #binary = file.read()
            b64string = base64.b64encode(binary).decode("utf-8")

        os.remove(file.filename)
        data = request.form
        user = request.cookies["email"]
        vehiclename = data["name"]
        description = data["description"]
        price = int(data["price"])
        category = data["category"]
        tags = data["tags"]

        print(user, vehiclename, description, price, category, tags)

        if user == None or vehiclename == None or description == None or price == None or category == None:
            return redirect("/upload")
        
        if "#" in tags:
            allTags = tags.split(" ")
            for i in range(len(allTags)):
                if allTags[i][0] != "#" or len(allTags[i]) < 2:
                    return redirect("/upload")
            
        data = {
            "user":user,
            "image": b64string,
            "vehicle":vehiclename,
            "description":description,
            "price":price,
            "category":category,
            "tags":tags
        }
        
        uploaded = database.UploadVehicle(data)
        print(uploaded)
        #ADD ANOTHER ENTRY TO UPLOAD THE VEHICLE TO THE USER'S PROFILE
        return redirect("/page")
