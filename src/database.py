import os
from dotenv import load_dotenv
load_dotenv()
from pymongo import MongoClient

PORT = os.getenv("PORT")
DBURL = os.getenv("DBURL")

client = MongoClient(DBURL)
db = client.get_database("ranking")

