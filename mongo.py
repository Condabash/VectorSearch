# Mongo Connection #

# Import Packages
from pymongo import MongoClient
import env as e

# Get Env Variables
mongo_uri = e.mongo_uri
mongo_db = e.mongo_db
mongo_collection = e.mongo_collection

# Connect to MongoDB
client = MongoClient(mongo_uri)  # Client
db = client[mongo_db]  # DB
collection = db[mongo_collection]  # Collection
