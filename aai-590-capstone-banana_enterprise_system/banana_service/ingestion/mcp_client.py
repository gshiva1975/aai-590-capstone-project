# banana_service/ingestion/mcp_client.py

import requests

class MCPClient:
    def __init__(self, url):
        self.url = url

    def call(self, method, params=None):
        response = requests.post(
            self.url,
            json={
                "method": method,
                "params": params or {}
            }
        )
        return response.json()

