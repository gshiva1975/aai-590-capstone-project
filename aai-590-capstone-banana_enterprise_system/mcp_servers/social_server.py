
from base_mcp import BaseMCPServer

def fetch_social_sentiment(ticker="AAPL"):
    return [
        f"{ticker} trending positively on forums",
        f"High retail engagement post earnings"
    ]

server = BaseMCPServer("Social")
server.register_tool("fetch_social_sentiment", fetch_social_sentiment)
app = server.app
