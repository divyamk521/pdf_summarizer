def chunk_text(text: str, chunk_size: int = 1500, overlap: int = 200):
    if not text:
        return []

    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = min(start + chunk_size, text_length)
        chunk = text[start:end].strip()

        if chunk:  # avoid empty chunks
            chunks.append(chunk)

        start += chunk_size - overlap

    print(f"Total chunks created: {len(chunks)}")  # 🔥 debug

    return chunks