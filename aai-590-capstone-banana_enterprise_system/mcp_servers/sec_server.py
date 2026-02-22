
from base_mcp import BaseMCPServer

def fetch_sec_filings(ticker="AAPL"):
    return [
        f"{ticker} revenue grew 15% year over year",
        f"{ticker} operating margin improved"
    ]

server = BaseMCPServer("SEC")
server.register_tool("fetch_sec_filings", fetch_sec_filings)
app = server.app
