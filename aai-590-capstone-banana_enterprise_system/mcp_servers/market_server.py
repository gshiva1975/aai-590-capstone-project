# mcp_servers/market_server.py

from mcp_servers.base_mcp import BaseMCP
import requests

mcp = BaseMCP()

def fetch_market_data(ticker: str):
    # Example: Alpha Vantage API
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey=YOUR_API_KEY"
    response = requests.get(url)

    if response.status_code != 200:
        return []

    data = response.json()

    # Simplified summary
    return [f"{ticker} shows high trading volume trend"]

mcp.register("fetch_market_data", fetch_market_data)

app = mcp.app

