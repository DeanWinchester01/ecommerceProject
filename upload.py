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
        print(b62string)
            
            
        data = {
            "user":"someone",
            "image": b62string
        }

        database.UploadVehicle(data)
        return redirect("/upload")
