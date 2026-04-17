from app.services.chunk_service import chunk_text
from app.services.ollama_service import generate_summary

def summarize_text(text: str, mode: str = "brief", model: str = "tinyllama"):
    chunks = chunk_text(text, chunk_size=1000, overlap=100)

    if not chunks:
        return "No text found in PDF."

    first_chunk = chunks[0]

    print(f"Processing with model: {model} | mode: {mode}")

    summary = generate_summary(
        text=first_chunk,
        mode=mode,
        model=model
    )

    return summary