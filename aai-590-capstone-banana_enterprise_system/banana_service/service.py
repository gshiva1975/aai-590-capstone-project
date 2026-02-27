# banana_service/service.py

#from banana_service.ingestion.mcp_client import MCPClient
from banana_service.core.embedding_model import EmbeddingModel
from banana_service.core.vector_store import VectorStore
from banana_service.agents.orchestrator import Orchestrator
from banana_service.agents.reflection import ReflectionAgent 
from banana_service.agents.researcher import ResearcherAgent 
from banana_service.agents.analyst import AnalystAgent 
from banana_service.agents.scribe import ScribeAgent 
from banana_service.config import settings


class BananaService:
    def __init__(self):
        self.embed = EmbeddingModel("sentence-transformers/all-MiniLM-L6-v2")
        self.vector_store = VectorStore()

        researcher = ResearcherAgent(self.vector_store, self.embed)
        analyst = AnalystAgent()
        reflection = ReflectionAgent()
        scribe = ScribeAgent()

        self.workflow = Orchestrator(
            researcher,
            analyst,
            reflection,
            scribe,
            threshold=0.75
        )

        self._load_initial_data()

    def _load_initial_data(self):
        docs = [
            "Apple revenue increased 12% year-over-year.",
            "RSI indicates moderate overbought conditions.",
            "Investor sentiment trending positive in forums."
        ]

        vectors = [self.embed.encode(d) for d in docs]
        self.vector_store.add(vectors, docs)

    def analyze(self, query: str):
        return self.workflow.run(query)

