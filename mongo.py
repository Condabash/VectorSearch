# Mongo Connection #

# Import Packages
from pymongo import MongoClient
import env as e

# Get MongoDB URI
mongo_uri = e.mongo_uri

# Connect to MongoDB
client = MongoClient(mongo_uri)  # Client
db = client.sample_mflix  # DB
collection = db.movies  # Collection
