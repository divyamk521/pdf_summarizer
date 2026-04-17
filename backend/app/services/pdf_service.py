from pypdf import PdfReader

def extract_pdf_data(file):
    reader = PdfReader(file.file)

    text_parts = []

    for i, page in enumerate(reader.pages):
        page_text = page.extract_text()

        if page_text:
            text_parts.append(page_text)
        else:
            print(f"Warning: Page {i+1} has no extractable text")

    full_text = "\n".join(text_parts)

    metadata = reader.metadata or {}

    return {
        "text": full_text,
        "page_count": len(reader.pages),
        "author": metadata.get("/Author"),
        "title": metadata.get("/Title"),
    }