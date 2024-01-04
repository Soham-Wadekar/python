# Schema validation lets you create validation rules for your fields, such as allowed data types and value ranges.

from config.main import client

db = client.library

book_validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["title", "authors", "publication_date", "genre", "copies_sold"],
        "properties": {
            "title": {
                "bsonType": "string",
                "description": "must be a string and it is required",
            },
            "authors": {
                "bsonType": "array",
                "items": {
                    "bsonType": "objectId",
                    "description": "must be objectId and it is required",
                },
            },
            "publication_date": {
                "bsonType": "date",
                "description": "must be a date and it is required",
            },
            "genre": {
                "enum": ["Fiction", "Non-Fiction"],
                "description": "can only be one of the enum values and it is required",
            },
            "copies_sold": {
                "bsonType": "int",
                "minimum": 0,
                "description": "must be an integer greater than 0 and it is required",
            },
        },
    }
}

try:
    db.create_collection("books")
except Exception as e:
    print(e)

db.command("collMod", "books", validator=book_validator)

# -----------------------------------------------------------------------------------------

author_validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["name", "date_of_birth"],
        "properties": {
            "name": {
                "bsonType": "string",
                "description": "must be a string and it is required",
            },
            "date_of_birth": {
                "bsonType": "date",
                "description": "must be a date and it is required",
            },
        },
    }
}

try:
    db.create_collection("authors")
except Exception as e:
    print(e)

db.command("collMod", "authors", validator=author_validator)
