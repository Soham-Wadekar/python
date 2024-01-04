from config.main import client
from bson.objectid import ObjectId

db = client.employees
collection = db.people

# person = {
#     "_id": ObjectId("5f1c6abf7461333032a53a00"),
#     "name": "Jane Doe",
#     "age": 32
# }
# collection.insert_one(person)

address = {
    "_id": ObjectId("5f1c6abf7461444032a53a62"),
    "street": "123 Main Street",
    "city": "Cityville",
    "state": "Stateville",
    "postalCode": "12345",
    "country": "Countryland",
}

# METHOD 1 (Embedded Documents)
_id = ObjectId("5f1c6abf7461444032a53a00")
collection.update_one({"_id": _id}, {"$addToSet": {"address": address}})

# METHOD 2 (Relationships)
_id = ObjectId("5f1c6abf7461333032a53a00")

address = address.copy()
address["owner_id"] = ObjectId("5f1c6abf7461333032a53a00")

address_collection = db.addresses
address_collection.insert_one(address)
