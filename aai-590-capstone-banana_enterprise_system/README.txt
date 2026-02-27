
python3 -m venv venv
source venv/bin/activate   

pip install -r requirements.txt


Terminal 1 — SEC MCP
servers
uvicorn sec_server:app --port 8001

Terminal 2 — Market MCP
cd mcp_servers
uvicorn market_server:app --port 8002

Terminal 3 — Social MCP
cd mcp_servers
uvicorn social_server:app --port 8003

🚀
Run MCP servers:
uvicorn mcp_servers.sec_server:app --port 8001
uvicorn mcp_servers.market_server:app --port 8002
uvicorn mcp_servers.social_server:app --port 8003

Run API:
uvicorn banana_service.main:app --reload

Sample Request:
POST /analyze
{
  "query": "Is AAPL a good investment?"
}

Trace Flow:
API → Service → MCP → RAG → FinBERT → Reflection → Scribe → Response
