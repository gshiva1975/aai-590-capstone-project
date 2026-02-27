
class Settings:
    MCP_SEC_URL = "http://localhost:8001/mcp"
    MCP_MARKET_URL = "http://localhost:8002/mcp"
    MCP_SOCIAL_URL = "http://localhost:8003/mcp"
    MCP_SEC_URL = None
    MCP_MARKET_URL = None
    MCP_SOCIAL_URL = None
    EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
    FIN_MODEL = "ProsusAI/finbert"
    CONFIDENCE_THRESHOLD = 0.75

settings = Settings()
