from pathlib import Path
from uuid import uuid4
from fastapi import APIRouter, File, HTTPException, UploadFile
from app.services.pdf_extractor import extract_pdf_text

router = APIRouter()
UPLOAD_DIR = Path("backend/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
@router.post("/documents/upload")
async def upload_document(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported.",
        )

    file_id = uuid4()

    document_dir = UPLOAD_DIR / str(file_id)
    document_dir.mkdir(parents=True, exist_ok=True)

    file_path = document_dir / "original.pdf"

    contents = await file.read()
    file_path.write_bytes(contents)

    extracted_text = extract_pdf_text(file_path)

    text_path = document_dir / "extracted.txt"
    text_path.write_text(extracted_text, encoding="utf-8")

    return {
        "message": "Document uploaded successfully",
        "document_id": str(file_id),
        "filename": file.filename,
        "content_type": file.content_type,
        "size": len(contents),
    }   