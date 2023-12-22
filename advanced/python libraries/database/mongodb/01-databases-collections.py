from config.main import client

# List all databases
dbs = client.list_database_names()
print(f"List of databases: {dbs}")

# Getting a particular database
test_db = client.test

# Listing all the collections in a particular database
collections = test_db.list_collection_names()
print(f"Collections in database '{test_db.name}' are {collections}")
