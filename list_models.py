import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()

API_KEY = os.getenv("API_KEY")

headers = {
    "Authorization" : f"Bearer {API_KEY}",
    "Content-Type" : "application/json"
}

url = "https://api.groq.com/openai/v1/models"

response = requests.get(url,headers=headers)

data = response.json()

print(json.dumps(data,indent=4))