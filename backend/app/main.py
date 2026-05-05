from fastapi import FastAPI, UploadFile, File, HTTPException

from fastapi.middleware.cors import CORSMiddleware

from .utils import extract_text_from_pdf, chunk_text

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB

@app.post("/documents/upload")
async def upload_document(file: UploadFile = File(...)):
    allowed_types = {
        "text/plain",
        "application/pdf",
    }

    if file.content_type not in allowed_types:
        raise HTTPException(status_code=400, detail="Unsupported file type")

    content = await file.read()

    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail="File too large")

    if file.content_type == "text/plain":
        text = content.decode("utf-8", errors="replace")

    elif file.content_type == "application/pdf":
        text = extract_text_from_pdf(content)

    # Then chunk the text and store it
    chunks = chunk_text(text)

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "num_chars": len(text),
        "num_chunks": len(chunks),
    }