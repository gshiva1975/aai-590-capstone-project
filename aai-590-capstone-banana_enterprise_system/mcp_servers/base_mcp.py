
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Callable, Optional, Any
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("MCP")

class MCPRequest(BaseModel):
    method: str
    params: Optional[Dict[str, Any]] = {}

class BaseMCPServer:
    def __init__(self, name):
        self.name = name
        self.app = FastAPI(title=f"{name} MCP Server")
        self.tools: Dict[str, Callable] = {}
        self._register_routes()

    def register_tool(self, name, func):
        logger.info(f"[{self.name}] Registered tool: {name}")
        self.tools[name] = func

    def _register_routes(self):

        @self.app.post("/mcp")
        def handle(req: MCPRequest):
            logger.info(f"[{self.name}] Method called: {req.method}")
            if req.method not in self.tools:
                return {"error": "Unknown method"}
            result = self.tools[req.method](**req.params)
            return {"result": result}
