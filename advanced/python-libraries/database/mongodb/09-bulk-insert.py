from config.main import client
from datetime import datetime as dt

db = client.library

book_collection = db.books
author_collection = db.authors

authors_list = [
    {
        "name": "Author 1",
        "date_of_birth": dt(1775, 12, 16)
    },
    {
        "name": "Author 2",
        "date_of_birth": dt(1812, 2, 7)
    },
    {
        "name": "Author 3",
        "date_of_birth": dt(1835, 11, 30)
    },
    {
        "name": "Author 4",
        "date_of_birth": dt(1890, 9, 15)
    },
    {
        "name": "Author 5",
        "date_of_birth": dt(1927, 3, 6)
    },
    {
        "name": "Author 6",
        "date_of_birth": dt(1892, 1, 3)
    },
]

author_ids = author_collection.insert_many(authors_list).inserted_ids

books_list = [
    {
        "title": "Book 1",
        "authors": [author_ids[0]],
        "publication_date": dt(1821, 3, 21),
        "genre": "Non-Fiction",
        "copies_sold": 10_000_000
    },
    {
        "title": "Book 2",
        "authors": [author_ids[0], author_ids[1]],
        "publication_date": dt(1842, 12, 27),
        "genre": "Fiction",
        "copies_sold": 15_000
    },
    {
        "title": "Book 3",
        "authors": [author_ids[3]],
        "publication_date": dt(1920, 7, 31),
        "genre": "Non-Fiction",
        "copies_sold": 50_000
    },
    {
        "title": "Book 4",
        "authors": [author_ids[2]],
        "publication_date": dt(1869, 10, 11),
        "genre": "Non-Fiction",
        "copies_sold": 1_000_000
    },
    {
        "title": "Book 5",
        "authors": [author_ids[4], author_ids[5]],
        "publication_date": dt(1954, 3, 21),
        "genre": "Fiction",
        "copies_sold": 20_000_000
    },
]

book_collection.insert_many(books_list)