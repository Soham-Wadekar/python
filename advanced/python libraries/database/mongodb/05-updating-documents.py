from config.main import client
from bson.objectid import ObjectId

db = client.forest
collection = db.animals

# Get animal by id
doc_id = "6585591ae84db2ec6f1e622d"
_id = ObjectId(doc_id)

updates = {
    "$set": {"has_trunk": True},
    "$inc": {"weight": 100},
    "$rename": {"name": "animal_name"}
}

# Update the document
collection.update_one({"_id": _id}, updates)

# Remove a field of the document
collection.update_one({"_id": _id}, {"$unset": {"has_trunk": ""}})

# Change fields of existing documents
changes = {
    "name": "Elephant",
    "weight": 5000,
    "sound": "Trumpet"
}

collection.replace_one({"_id": _id}, changes)