
from base_mcp import BaseMCPServer

def fetch_market_data(ticker="AAPL"):
    return [
        f"{ticker} RSI bullish at 68",
        f"{ticker} volume breakout observed"
    ]

server = BaseMCPServer("Market")
server.register_tool("fetch_market_data", fetch_market_data)
app = server.app
