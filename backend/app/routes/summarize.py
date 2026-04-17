from fastapi import APIRouter, UploadFile, File, Form
from app.services.pdf_service import extract_pdf_data
from app.services.summary_service import summarize_text

router = APIRouter()

@router.post("/summarize")
async def summarize_pdf(
    file: UploadFile = File(...),
    mode: str = Form("brief")
):
    data = extract_pdf_data(file)

    final_summary = summarize_text(
        text=data["text"],
        mode=mode
    )

    return {
        "pages": data["page_count"],
        "mode": mode,
        "summary": final_summary
    }