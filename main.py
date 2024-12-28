# Main Code #

# Import Packages
from generate import generate_embedding
from mongo import collection
import env as e

# Get Env Variables
model = e.model
field = e.field
index = e.index

# User Query
query = "Give me objects having year 1903 and rated TV-G or Passed"

# Generate Embedding For Query
query_embedding = generate_embedding(query)

# Print Query Embedding
print(query_embedding)

# Search Collection
results = collection.aggregate(
    [
        {
            "$vectorSearch": {
                "queryVector": query_embedding,
                "path": field,
                "numCandidates": 50, # Number of Candidates 
                "limit": 50, # Number of Results
                "index": index,  # Search Index Name
            }
        }
    ]
)

# Print User Query
print("\n# User Query #\n")
print(f"Query: {query}")

# Print Embedding Model
if model == "hf":
    print("\n# Hugging Face Embedding Model #\n")
else:
    print("\n# OpenAI Embedding Model #\n")

# Print Results
for index, document in enumerate(results):
    # Print Object Index
    print(f' Object-{index}:')

    # Print Document
    print(document['_id'])
