# Gererate Embeddings #

# Import Packages
import requests
import openai
from mongo import collection
import env as e

# Get Env Variables
hf_token = e.hf_token
hf_embedding_url = e.hf_embedding_url
openai_api_key = e.openai_api_key
openai_model = e.openai_model
model = e.model
field = e.field

# Set OpenAI API Key
openai.api_key = openai_api_key

# Generate Embedding Function
def generate_embedding(text: str) -> list[float]:
    # Using Hugging Face Model
    if model == "hf":
        # Generate Embedding Response
        response = requests.post(
            hf_embedding_url,
            headers={"Authorization": f"Bearer {hf_token}"},
            json={"inputs": text},
        )

        # Check Response Status Code
        if response.status_code != 200:
            raise ValueError(
                f"Request failed with status code {response.status_code}: {response.text}"
            )

        # Return Embedding Response
        return response.json()

    # Using OpenAI Model
    else:
        # Generate Embedding Response
        response = openai.embeddings.create(model=openai_model, input=text)

        # Return Embedding Response
        return response.data[0].embedding


# Add Embedding To Collection Function
def add_embedding():
    # Get Documents
    documents = collection.find({"plot": {"$exists": True}}).limit(50)
    for document in documents:
        embedding = generate_embedding(document["plot"])
        collection.update_one(
            {"_id": document["_id"]},
            {"$set": {field: embedding}},
        )

    # Print Success Message
    print("Embeddings added successfully!")
