
from banana_service.config import settings
from banana_service.ingestion.mcp_client import MCPClient
from banana_service.core.vector_store import VectorStore
from banana_service.core.embedding_model import EmbeddingModel
from banana_service.core.financial_model import FinancialSentimentModel
from banana_service.agents.researcher import ResearcherAgent
from banana_service.agents.analyst import AnalystAgent
from banana_service.agents.reflection import ReflectionAgent
from banana_service.agents.scribe import ScribeAgent
from banana_service.agents.orchestrator import BananaOrchestrator
from logger import setup_logger

logger = setup_logger("Service")

class BananaService:
    def __init__(self):
        logger.info("Initializing service")
        self.sec = MCPClient(settings.MCP_SEC_URL)
        self.market = MCPClient(settings.MCP_MARKET_URL)
        self.social = MCPClient(settings.MCP_SOCIAL_URL)

        self.embed = EmbeddingModel(settings.EMBEDDING_MODEL)
        self.model = FinancialSentimentModel(settings.FIN_MODEL)
        self.store = VectorStore()

        self._load_data()

        researcher = ResearcherAgent(self.store, self.embed)
        analyst = AnalystAgent(self.model)
        reflection = ReflectionAgent()
        scribe = ScribeAgent()

        self.workflow = BananaOrchestrator(
            researcher, analyst, reflection, scribe,
            settings.CONFIDENCE_THRESHOLD
        )

    def _load_data(self):
        logger.info("Loading MCP data")
        docs = (
            self.sec.call("fetch_sec_filings") +
            self.market.call("fetch_market_data") +
            self.social.call("fetch_social_sentiment")
        )
        vectors = [self.embed.encode(d) for d in docs]
        self.store.add(vectors, docs)

    def analyze(self, query):
        return self.workflow.run(query)
