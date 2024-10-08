from pymongo import MongoClient
import ssl

# Connect to the MongoDB server
print("1")
client = MongoClient(
    "mongodb+srv://jeznerleonidas0:jwduC3xdsqb9SagF@ecommerceproject.sznvj.mongodb.net/?retryWrites=true&w=majority&appName=eCommerceProject",
    tls=True,                     # Enable TLS
    tlsAllowInvalidCertificates=True  # Disable SSL certificate verification
)

# Access the database
print("2")
database = client["eCommerceProject"]

# Access the collection
print("3")
collection = database["vehicles"]

# Insert a single document
print("4")
result = collection.insert_one({"x": 1})
print("Document inserted, acknowledged:", result.acknowledged)

# You can also insert multiple documents as shown below:
document_list = [
    {"name": "Mongo's Burgers"},
    {"name": "Mongo's Pizza"}
]

# Insert multiple documents
result = collection.insert_many(document_list, bypass_document_validation=True)
print(f"{len(result.inserted_ids)} documents inserted.")

print("5")
