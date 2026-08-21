from pathlib import Path
from uuid import uuid4

from fastapi import APIRouter, File, HTTPException, UploadFile


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
    file_path = UPLOAD_DIR / f"{file_id}.pdf"

    contents = await file.read()
    file_path.write_bytes(contents)

    return {
        "message": "Document uploaded successfully",
        "document_id": str(file_id),
        "filename": file.filename,
        "content_type": file.content_type,
        "size": len(contents),
    }