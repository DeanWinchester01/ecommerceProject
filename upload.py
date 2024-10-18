import os
from flask import Flask, Blueprint, render_template, request, redirect
from werkzeug.utils import secure_filename
import database
import io
import base64
from PIL import Image
from encryption import DecryptMessage

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "flaskenv/ecommerceProject/static/images/"

uploadBP = Blueprint("upload",__name__)
specialChars = {
    "ä":"a",
    "å":"a",
    "ö":"o"
}

@uploadBP.route("/upload", methods = ["GET","POST"])
def UploadVehicle():
    return render_template("upload.html")

@uploadBP.route("/upload/vehicle", methods = ["GET","POST"])
def GetVehicleImage():
    if request.method == "POST":
        file = request.files["image"]
        filename = secure_filename(file.filename)
        os.mkdir("ecommerceProject/static","uploads")
        file_path = os.path.join("ecommerceProject", "static", "uploads", filename)
        file.save(file_path)
        #file.save("ecommerceProject\\static\\uploads\\"+secure_filename(file.filename))
        #file.filename = "ecommerceProject\\" + file.filename
        #file.filename = file.filename.replace("\\","/")
                
        b64string = ""

        with Image.open(file_path) as img:
            buffered = io.BytesIO()
            img.save(buffered, format="PNG")
            binary = buffered.getvalue()
            #binary = file.read()
            b64string = base64.b64encode(binary).decode("utf-8")

        #os.remove(file.filename)
        data = request.form
        user = request.cookies["email"]
        vehiclename = data["name"]
        description = data["description"]
        price = int(data["price"])
        category = data["category"]
        tags = data["tags"]

        #print(user, vehiclename, description, price, category, tags)

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
            "name":vehiclename,
            "description":description,
            "price":price,
            "category":category,
            "tags":tags
        }
        
        uploaded = database.UploadVehicle(data)
        users = database.GetUsers()

        for user in users.find():
            foundEmail = DecryptMessage(user["email"])
            
            if foundEmail != request.cookies.get("email"):
                continue

            vehicles = []
            if "vehicles" in user:
                vehicles = user["vehicles"]
            
            vehicles.append(uploaded.inserted_id)
            updatefilter = {"_id": user["_id"]}
            update_operation = { '$set' : 
                { 'vehicles' : vehicles }
            }
            users.update_one(updatefilter, update_operation)

            os.rmdir(os.path.join("ecommerceProject/static","uploads"))
        return redirect("/page")
