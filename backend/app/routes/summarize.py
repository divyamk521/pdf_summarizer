from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import StreamingResponse
from app.services.pdf_service import extract_pdf_data
from app.services.chunk_service import chunk_text
from app.services.ollama_service import stream_summary

router = APIRouter()

@router.post("/summarize-stream")
async def summarize_pdf_stream(
    file: UploadFile = File(...),
    mode: str = Form("brief"),
    model: str = Form("tinyllama")
):
    data = extract_pdf_data(file)

    chunks = chunk_text(data["text"])

    first_chunk = chunks[0]

    generator = stream_summary(first_chunk, mode=mode, model=model)

    return StreamingResponse(generator, media_type="text/plain")