import os
from flask import Flask, Blueprint, render_template, request, redirect
from werkzeug.utils import secure_filename
import database
import io
import base64

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
        binary = file.read()
        b62string = base64.b32encode(binary).decode("utf-8")
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
        
        allTags = tags.split(" ")
        for i in range(len(allTags)):
            if allTags[i][0] != "#" or len(allTags[i]) < 2:
                return redirect("/upload")
            
        data = {
            "user":user,
            "image": b62string,
            "vehicle":vehiclename,
            "description":description,
            "price":price,
            "category":category,
            "tags":tags
        }
        
        database.UploadVehicle(data)
        #ADD ANOTHER ENTRY TO UPLOAD THE VEHICLE TO THE USER'S PROFILE
        return redirect("/page")
