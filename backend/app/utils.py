import io
from pypdf import PdfReader

def extract_text_from_pdf(content: bytes) -> str:
    reader = PdfReader(io.BytesIO(content))

    texts = []
    for page in reader.pages:
        page_text = page.extract_text() or ""
        texts.append(page_text)

    return "\n\n".join(texts)

def chunk_text(text: str, chunk_size: int = 1200, overlap: int = 200) -> list[str]:
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap

    return chunks