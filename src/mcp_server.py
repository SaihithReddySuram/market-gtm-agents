from fastapi import FastAPI
from dotenv import load_dotenv
import requests
import os

load_dotenv()

app = FastAPI()

SERPAPI_KEY = os.getenv("SERPAPI_API_KEY")


@app.get("/")
def root():
    return {"message": "MCP Server Running"}


@app.get("/search")
def search(query: str):
    if not SERPAPI_KEY:
        return {"error": "SERPAPI_API_KEY missing in .env"}

    url = "https://serpapi.com/search"

    params = {
        "engine": "google",
        "q": query,
        "api_key": SERPAPI_KEY,
        "num": 5
    }

    response = requests.get(url, params=params, timeout=30)

    return response.json()