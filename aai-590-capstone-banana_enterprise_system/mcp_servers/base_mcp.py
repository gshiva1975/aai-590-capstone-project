# mcp_servers/base_mcp.py

from fastapi import FastAPI
from pydantic import BaseModel
import logging

class MCPRequest(BaseModel):
    method: str
    params: dict = {}

class BaseMCP:
    def __init__(self):
        self.app = FastAPI()
        self.tools = {}
        self._register_routes()

    def register(self, name, func):
        self.tools[name] = func

    def _register_routes(self):
        @self.app.post("/mcp")
        def handle(req: MCPRequest):
            if req.method not in self.tools:
                return {"error": "Method not found"}
            return self.tools[req.method](**req.params)

