from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"

class CompletionRequest(BaseModel):
    prompt: str
    max_tokens: int = 100

@app.post("/complete")
async def complete(req: CompletionRequest):
    payload = {
        "model": "deepseek-coder-v2:latest",
        "prompt": req.prompt,
        "stream": False,
        "options": {
            "num_predict": req.max_tokens
        }
    }
    response = requests.post(OLLAMA_ENDPOINT, json=payload)
    return response.json()
