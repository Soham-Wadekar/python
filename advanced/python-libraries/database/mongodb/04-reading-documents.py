from config.main import client
import pprint
from bson.objectid import ObjectId

printer = pprint.PrettyPrinter()

forest = client.forest
animals = forest.animals

# Get all the documents
all_animals = animals.find()

for animal in all_animals:
    printer.pprint(animal)

# Get a specific document based on the key - First document that matches the criteria
roaring_animals = animals.find_one({"name": "Lion", "sound": "Roar"})
printer.pprint(roaring_animals)

# Get counts of documents

count_all = animals.count_documents(filter={})
print(f"Total no. of documents: {count_all}")

count_roars = animals.count_documents(filter={"sound": "Roar"})
print(f"No. of documents which has sound roar: {count_roars}")

# Get document by ID
doc_id = "6585591ae84db2ec6f1e622d"
_id = ObjectId(doc_id)

animal = animals.find_one({"_id": _id})
printer.pprint(animal)

# Get the documents within the specific range
query = {"$and": [{"weight": {"$gte": 50}}, {"weight": {"$lt": 1000}}]}

animal = animals.find(query).sort("weight")
for anim in animal:
    printer.pprint(anim)

# Get specific columns
columns_to_be_displayed = {"_id": 0, "name": 1, "habitat": 1}
all_animals = animals.find({}, columns_to_be_displayed)
for animal in all_animals:
    print(animal)
