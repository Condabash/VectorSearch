# Test Code #

# Import Packages
from generate import generate_embedding
from mongo import collection
from pprint import pprint


## Test Mongo Connection

# Check Cursor Object
items = collection.find().limit(5)
print("Cursor Object: ", items)

# Print Collection Data
for index, item in enumerate(items):
    print(f"\nObject-{index}:")  # Object Index
    pprint(item)  # Object


## Test Embedding Generation

# Generate Embedding
embeddings = generate_embedding("Suraj is coder!")  # Generate
pprint(embeddings)  # Print


## Test Data Query

# Print first 50 documents with plot from collection
documents = collection.find({"plot": {"$exists": True}}).limit(50)
print("Cursor Object: ", documents)
documents_list = list(documents)
documents_count = len(documents_list)
print("Documents Count: ", documents_count)
