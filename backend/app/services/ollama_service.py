import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"


def build_prompt(text: str, mode: str):
    if mode == "brief":
        return f"""
You are a professional summarizer.

Summarize the following text in 3-4 clear sentences.
Ignore names, credits, metadata, or irrelevant details.
Focus only on the core meaning.

TEXT:
{text}
"""

    elif mode == "detailed":
        return f"""
Provide a detailed and well-structured summary of the following text.
Focus on key ideas, concepts and explanations.

TEXT:
{text}
"""

    elif mode == "bullet":
        return f"""
Summarize the following text into clear bullet points.
Avoid unnecessary names or credits.

TEXT:
{text}
"""

    elif mode == "executive":
        return f"""
Provide an executive-level summary.
Make it concise, professional, and business-friendly.

TEXT:
{text}
"""

    return text


def stream_summary(text: str, mode: str = "brief", model: str = "tinyllama"):
    prompt = build_prompt(text, mode)

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": model,
            "prompt": prompt,
            "stream": True
        },
        stream=True
    )

    if response.status_code != 200:
        yield "⚠️ Error generating summary"
        return

    for line in response.iter_lines():
        if line:
            try:
                decoded = line.decode("utf-8")
                data = json.loads(decoded)   # ✅ FIXED (was eval)

                if "response" in data:
                    yield data["response"]

            except Exception as e:
                print("STREAM ERROR:", e)
                continue