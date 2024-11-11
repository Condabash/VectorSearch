# Env #

# Import Packages
import os
from dotenv import load_dotenv, find_dotenv

# Load Env
load_dotenv(find_dotenv())

# Get Env Variables

# MongoDB URI
mongo_uri = os.getenv("MONGO_URI")

# HF Access Token
hf_token = os.getenv("HF_TOKEN")

# HF Embedding URL
hf_embedding_url = os.getenv("HF_EMBEDDING_URL")

# OpenAI API Key
openai_api_key = os.getenv("OPENAI_API_KEY")

# OpenAI Embedding Model
openai_model = os.getenv("OPENAI_MODEL")

# Embedding Generation Model
model = os.getenv("MODEL")

# Collection Embedding Field
field = os.getenv("FIELD")

# Atlas Search Index Name
index = os.getenv("INDEX")

# Print Env Variables
# print("MongoDB URI:", mongo_uri)
# print("HF Token:", hf_token)
# print("HF Embedding URL:", hf_embedding_url)
# print("OpenAI API Key:", openai_api_key)
# print("OpenAI Model:", openai_model)
# print("Model:", model)
# print("Field:", field)
# print("Index:", index)
