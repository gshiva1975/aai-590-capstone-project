from fastapi import FastAPI
from banana_service.service import BananaService
from banana_service.llm import LocalLlamaLLM
from banana_service.config import settings

app = FastAPI()

my_llm = LocalLlamaLLM()

if settings.EXPERIMENT_MODE == "BASELINE":

    banana_service = BananaService(
        llm=my_llm
    )

elif settings.EXPERIMENT_MODE == "OPTIMIZED":

    from banana_service.core.vector_store import VectorStore
    from banana_service.core.embedding_model import EmbeddingModel
    from banana_service.agents.researcher import ResearcherAgent

    my_store = VectorStore(dim=384)
    my_embedder = EmbeddingModel()
    my_researcher = ResearcherAgent(my_store, my_embedder)

    banana_service = BananaService(
        llm=my_llm,
        store=my_store,
        embed=my_embedder,
        researcher_agent=my_researcher
    )

else:
    raise ValueError(f"Unsupported EXPERIMENT_MODE: {settings.EXPERIMENT_MODE}")


@app.post("/analyze")
def analyze(request: dict):
    query = request["query"]
    return banana_service.analyze(query)
