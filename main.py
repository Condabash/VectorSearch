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
query = "Imaginary characters from outer space at war."

# Generate Embedding For Query
query_embedding = generate_embedding(query)

# Search Collection
results = collection.aggregate(
    [
        {
            "$vectorSearch": {
                "queryVector": query_embedding,
                "path": field,
                "numCandidates": 100,
                "limit": 4,  #
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
    print(
        f'{index}. \nMovie Name: {document["title"]} \nMovie Plot: {document["plot"]}\n'
    )
