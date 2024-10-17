from pymongo import MongoClient

from encryption import EncryptMessage, DecryptMessage
import os
import io
from flask import Flask
import base64
from PIL import Image

# Connect to the MongoDB server
print("[MongoDB] 1: Database Server Connection Check")
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

def GetVehicles():
    # Access the collection
    print("[MongoDB] 2: Database Collection Access Check")
    collection = client["eCommerceProject"]["vehicles"]

    # Insert a single document
    data = []
    #result = collection.insert_one({"x": 1})
    for x in collection.find():
        data.append(x)

    return data

    # You can also insert multiple documents as shown below:
    document_list = [
        {"vehicle": "car", "seller": "nico", "year":2001},
    ]
    entries = [
        {
            "name":"Yamaha YZF-R7 R7 HO 2023",
            "category":"Motorbike",
            "description":"N/A",
            "price":16099
        },
        {
            "name":"Yamaha YZF-R3 2024",
            "category":"Motorbike",
            "description":"N/A",
            "price":9675
        },
        {
            "name":"Yamaha YZ450FX",
            "category":"Motorbike",
            "description":"N/A",
            "price":16249
        },
        {
            "name":"Yamaha XSR900 GP 2024",
            "category":"Motorbike",
            "description":"N/A",
            "price":22799
        },
        {
            "name":"Yamaha Tenere 700 2024",
            "category":"Motorbike",
            "description":"N/A",
            "price":20180
        },
        {
            "name":"Yamaha AG125 2023",
            "category":"Motorbike",
            "description":"N/A",
            "price":5299
        },
        {
            "name":"Yamaha MT-07 2023",
            "category":"Motorbike",
            "description":"N/A",
            "price":14099
        },
        {
            "name":"Kawasaki ZX6R Ninja 636 2024",
            "category":"Motorbike",
            "description":"N/A",
            "price":21495
        },
        {
            "name":"Kawasaki Z1000 ABS 2024",
            "category":"Motorbike",
            "description":"N/A",
            "price":19916
        },
        {
            "name":"Kawasaki KX85 Big Wheel 2024",
            "category":"Motorbike",
            "description":"N/A",
            "price":8495
        },
        {
            "name":"Kawasaki KLE300 Versys-X 300 2024",
            "category":"Motorbike",
            "description":"N/A",
            "price":9060
        },
        {
            "name":"Kawasaki EX500 Ninja 500 2024",
            "category":"Motorbike",
            "description":"N/A",
            "price":8995
        },
        {
            "name":"Kawasaki EN650 Vulcan SE 2024",
            "category":"Motorbike",
            "description":"N/A",
            "price":12866
        },
        {
            "name":"2017 Honda Civic",
            "category":"Car",
            "description":"N/A",
            "price":16950
        },
        {
            "name":"2019 Jaguar F-Type",
            "category":"Car",
            "description":"N/A",
            "price":139990
        },
        {
            "name":"2022 Toyota Corolla",
            "category":"Car",
            "description":"N/A",
            "price":31980
        },
        {
            "name":"2022 Tesla Model Y",
            "category":"Car",
            "description":"N/A",
            "price":49990
        },
        {
            "name":"2024 Kia Sportage",
            "category":"Car",
            "description":"N/A",
            "price":39990
        },
        {
            "name":"2024 Volkswagen ID.4",
            "category":"Car",
            "description":"N/A",
            "price":53990
        },
        {
            "name":"2022 Hyundai Kona",
            "category":"Car",
            "description":"N/A",
            "price":33990
        },
        {
            "name":"2015 Nissan GTR",
            "category":"Car",
            "description":"N/A",
            "price":139990
        }

    ]

    print("adding image")
    for i in range(len(entries)):
        fullName = os.path.join(app.config["UPLOAD_FOLDER"], str(i)+".png")
        with Image.open(fullName) as img:
            buffered = io.BytesIO()
            img.save(buffered, format="PNG")
            binary = buffered.getvalue()

            #binary = img.tobytes()
            #compressed = zlib.compress(binary)
            b64string = base64.b64encode(binary).decode("utf-8")
            entries[i]["image"] = b64string
            print(str(i)+" done")
        
    print("inserting")
    collection.insert_many(entries)
    
    #read_img = matplotlib.image.imread('your_image.png')
    '''for i in range(len(entries)):
        file = request.files["image"]
        #file.save(secure_filename(file.filename))
        binary = file.read()
        b62string = base64.b64encode(binary).decode("utf-8")
        print(b62string)
            
            
        data = {
            "user":"someone",
            "image": b62string
        }

        database.UploadVehicle(data)
    '''
    # Insert multiple documents
    #result = collection.insert_many(entries, bypass_document_validation=True)
    #print(f"{len(result.inserted_ids)} documents inserted.")

    print("[MongoDB] 3: Database Final Check")
#GetVehicles()
def UploadVehicle(data):
    collection = client["eCommerceProject"]["vehicles"]
    result = collection.insert_one(data)
    return result



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