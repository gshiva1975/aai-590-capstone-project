
from fastapi import FastAPI
from pydantic import BaseModel
from banana_service.service import BananaService
from logger import setup_logger, generate_request_id

logger = setup_logger("API")

app = FastAPI(title="BANANA Enterprise Agentic AI")

service = BananaService()

class QueryRequest(BaseModel):
    query: str

@app.post("/analyze")
def analyze(req: QueryRequest):
    rid = generate_request_id()
    logger.info(f"[{rid}] Incoming request")
    result = service.analyze(req.query)
    logger.info(f"[{rid}] Completed")
    return result
