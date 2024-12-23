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

@uploadBP.route("/upload", methods = ["GET","POST"])
def UploadVehicle():
    if request.cookies.get("loggedIn") != "True":
        return redirect("/login")
    return render_template("upload.html")

@uploadBP.route("/update/<id>", methods = ["GET","POST"])
def UpdateVehicle(id):
    form = request.form
    name = form["name"]
    category = form["category"]
    description = form["description"]
    price = form["price"]
    tags = form["tags"]
    print(price)

    if "$" in price:
        price = price[1:]
    print(name, category, description, price, tags)

    data = {
        "name":name,
        "category":category,
        "description":description,
        "price": int(price),
        "tags":tags
    }

    database.UpdateVehicle(data, id)
    return redirect("/page/"+request.cookies.get("username"))

@uploadBP.route("/upload/vehicle", methods = ["GET","POST"])
def GetVehicleImage():
    
    if request.method == "POST":
        file = request.files["image"]
        filename = secure_filename(file.filename)

        if not os.path.exists("ecommerceProject\\static\\uploads"):
            os.mkdir("ecommerceProject\\static\\uploads")

        file_path = os.path.join("ecommerceProject", "static", "uploads", filename)
        file.save(file_path)
                
        b64string = ""

        with Image.open(file_path) as img:
            buffered = io.BytesIO()
            img.save(buffered, format="PNG")
            binary = buffered.getvalue()
            b64string = base64.b64encode(binary).decode("utf-8")

        data = request.form
        user = request.cookies["email"]
        vehiclename = data["name"]
        description = data["description"]
        price = data["price"]
        category = data["category"]
        tags = data["tags"]

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
        
        data,image = database.UploadVehicle(data)
        users = database.GetUsers()

        for user in users.find():
            foundEmail = DecryptMessage(user["email"])
            
            if foundEmail != request.cookies.get("email"):
                continue

            vehicles = []
            if "vehicles" in user:
                vehicles = user["vehicles"]
            
            vehicles.append(data.inserted_id)
            updatefilter = {"_id": user["_id"]}
            update_operation = { '$set' : 
                { 'vehicles' : vehicles }
            }
            users.update_one(updatefilter, update_operation)

            os.remove("ecommerceProject/static/uploads/" + filename)
            os.rmdir(os.path.join("ecommerceProject/static/", "uploads"))
        return redirect("/page")
