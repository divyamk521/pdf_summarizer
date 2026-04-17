import requests
import json
from app.core.prompts import SUMMARY_MODES

OLLAMA_URL = "http://localhost:11434/api/generate"

def stream_summary(text: str, mode: str = "brief", model: str = "tinyllama"):
    instruction = SUMMARY_MODES.get(mode, SUMMARY_MODES["brief"])

    prompt = f"""
{instruction}

Text:
{text[:800]}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": model,
            "prompt": prompt,
            "stream": True
        },
        stream=True
    )

    for line in response.iter_lines():
        if line:
            try:
                data = json.loads(line.decode("utf-8"))
                chunk = data.get("response", "")
                yield chunk
            except:
                continue