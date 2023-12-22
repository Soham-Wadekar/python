from config.main import client

test_db = client.test

collection = test_db.test

test_doc = {"name": "Jumbo", "type": "Elephant"}

collection.insert_one(test_doc)
