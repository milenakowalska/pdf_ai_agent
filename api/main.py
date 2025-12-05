from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Hackathon API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health():
    """Basic API liveness."""
    return {"status": "ok"}
