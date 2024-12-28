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

# Extract Value Helper Function
def extract_value(doc, path, default="NA"):
    # Return nested field safely
    keys = path.split('.')
    for key in keys:
        if isinstance(doc, dict):
            if key in doc:
                doc = doc[key]
            else:
                return default
        elif isinstance(doc, list) and key.isdigit():
            index = int(key)
            if 0 <= index < len(doc):
                doc = doc[index]
            else:
                return default
        else:
            return default
    return doc


# Object Counter
counter = 0

# Serialize Document Function
def serialize_document(doc) -> str:
    # Serialize all fields of the document
    text_representation = f"""
    _id: {extract_value(doc, '_id', 'NA')}
    Plot: {extract_value(doc, 'plot', 'NA')}
    Genres: {', '.join(extract_value(doc, 'genres', ['NA']))}
    Runtime: {extract_value(doc, 'runtime', 'NA')} minutes
    Rated: {extract_value(doc, 'rated', 'NA')}
    Cast: {', '.join(extract_value(doc, 'cast', ['NA']))}
    Num Mflix Comments: {extract_value(doc, 'num_mflix_comments', 'NA')}
    Poster: {extract_value(doc, 'poster', 'NA')}
    Title: {extract_value(doc, 'title', 'NA')}
    Full Plot: {extract_value(doc, 'fullplot', 'NA')}
    Languages: {', '.join(extract_value(doc, 'languages', ['NA']))}
    Released: {extract_value(doc, 'released', 'NA')}
    Directors: {', '.join(extract_value(doc, 'directors', ['NA']))}
    Writers: {', '.join(extract_value(doc, 'writers', ['NA']))}
    Awards Wins: {extract_value(doc, 'awards.wins', 'NA')}
    Awards Nominations: {extract_value(doc, 'awards.nominations', 'NA')}
    Awards Text: {extract_value(doc, 'awards.text', 'NA')}
    Last Updated: {extract_value(doc, 'lastupdated', 'NA')}
    Year: {extract_value(doc, 'year', 'NA')}
    IMDB Rating: {extract_value(doc, 'imdb.rating', 'NA')}
    IMDB Votes: {extract_value(doc, 'imdb.votes', 'NA')}
    IMDB ID: {extract_value(doc, 'imdb.id', 'NA')}
    Countries: {', '.join(extract_value(doc, 'countries', ['NA']))}
    Type: {extract_value(doc, 'type', 'NA')}
    Tomatoes Viewer Rating: {extract_value(doc, 'tomatoes.viewer.rating', 'NA')}
    Tomatoes Viewer Reviews: {extract_value(doc, 'tomatoes.viewer.numReviews', 'NA')}
    Tomatoes Critic Rating: {extract_value(doc, 'tomatoes.critic.rating', 'NA')}
    Tomatoes Critic Reviews: {extract_value(doc, 'tomatoes.critic.numReviews', 'NA')}
    Tomatoes Consensus: {extract_value(doc, 'tomatoes.consensus', 'NA')}
    Tomatoes Rotten: {extract_value(doc, 'tomatoes.rotten', 'NA')}
    Tomatoes Fresh: {extract_value(doc, 'tomatoes.fresh', 'NA')}
    Tomatoes Last Updated: {extract_value(doc, 'tomatoes.lastUpdated', 'NA')}
    Production: {extract_value(doc, 'tomatoes.production', 'NA')}
    """
    
    # Remove leading and trailing whitespaces
    text = text_representation.strip()

    # Print Object Counter
    global counter
    counter += 1
    print(counter)

    # Return Text Representation
    return text


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
    documents = collection.find({"_id": {"$exists": True}}).limit(50)

    # Loop through each document
    for document in documents:
        # Serialize the entire document
        serialized_document = serialize_document(document)

        # Generate Embedding for the serialized document
        embedding = generate_embedding(serialized_document)

        # Update the document with the generated embedding
        collection.update_one(
            {"_id": document["_id"]},
            {"$set": {field: embedding}},
        )

    # Print Success Message
    print("Embeddings added successfully!")