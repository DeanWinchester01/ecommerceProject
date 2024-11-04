from pymongo import MongoClient

from encryption import EncryptMessage, DecryptMessage
import os
import io
from flask import Flask
import base64
from PIL import Image

client = MongoClient(
    "mongodb+srv://jeznerleonidas0:jwduC3xdsqb9SagF@ecommerceproject.sznvj.mongodb.net/?retryWrites=true&w=majority&appName=eCommerceProject",
    tls=True,                         # Enable TLS
    tlsAllowInvalidCertificates=True  # Disable SSL certificate verification
)
app = Flask(__name__)
vehicles = os.path.join("ecommerceProject\\static","images")
app.config["UPLOAD_FOLDER"] = vehicles

def GetUsers():
    return client["eCommerceProject"]["users"]

def GetVehicles(search):
    collection = client["eCommerceProject"]["vehicles"]

    data = []
    if search == "public":
        for x in collection.find():
            data.append(x)
        
    else:
        for x in collection.find({"user":search}):
            data.append(x)
        

    return data

def UploadVehicle(data):
    collection = client["eCommerceProject"]["vehicles"]
    result = collection.insert_one(data)
    return result


def DeleteVehicle():
    collection = client["eCommerceProject"]["vehicles"]



def LogIn(email, password):
    collection = client["eCommerceProject"]["users"]
    for account in collection.find():
        mail = DecryptMessage(account["email"])
        _pass = DecryptMessage(account["pass"])
        user = DecryptMessage(account["username"])

        print(mail)
        print(_pass)
        data = {"email":mail, "username":user, "pass" : _pass}
        if mail == email and password == _pass:
            return data
    return False

def SignUp(username, email, password):
    collection = client["eCommerceProject"]["users"]

    emptyList = True

    for account in collection.find():
        emptyList = False
        mail = DecryptMessage(account["email"])
        user = DecryptMessage(account["username"])
        print(mail, user)

        if mail == email or username == user:
            print("details taken")
            return False
        
        email = EncryptMessage(email)
        username = EncryptMessage(username)
        password = EncryptMessage(password)
        
        result = collection.insert_one({"email":email, "username": username, "pass" : password})
        return result
    
    if emptyList:
        email = EncryptMessage(email)
        username = EncryptMessage(username)
        password = EncryptMessage(password)
        
        result = collection.insert_one({"email":email, "username": username, "pass" : password})
        return result