from dotenv import load_dotenv, find_dotenv
import os
from pymongo import MongoClient

load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")

connection = (
    f"mongodb+srv://sohamw03:{password}@soham.q9pdwbh.mongodb.net/?authSource=admin"
)
client = MongoClient(connection)
