from config.main import client
from bson.objectid import ObjectId

db = client.forest
collection = db.animals

# Get animal by id
doc_id = "6585591ae84db2ec6f1e622d"
_id = ObjectId(doc_id)

try:
    collection.delete_one({"_id": _id})
except:
    print("Id not present")
