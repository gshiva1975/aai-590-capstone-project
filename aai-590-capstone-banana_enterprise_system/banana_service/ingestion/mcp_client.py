
import requests
from logger import setup_logger

logger = setup_logger("MCPClient")

class MCPClient:
    def __init__(self, url):
        self.url = url

    def call(self, method, params=None):
        logger.info(f"Calling MCP method: {method}")
        response = requests.post(
            self.url,
            json={"method": method, "params": params or {}}
        )
        result = response.json().get("result", [])
        logger.info(f"Received {len(result)} documents")
        return result
