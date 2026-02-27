# mcp_servers/sec_server.py

from base_mcp import BaseMCP
import requests

mcp = BaseMCP()

def fetch_sec_filings(ticker: str):
    # Example: SEC EDGAR API
    url = f"https://data.sec.gov/submissions/CIK{ticker}.json"
    response = requests.get(url)

    if response.status_code != 200:
        return []

    data = response.json()
    filings = []

    for form in data["filings"]["recent"]["form"]:
        if form in ["10-K", "10-Q"]:
            filings.append(f"{ticker} filed {form}")

    return filings

mcp.register("fetch_sec_filings", fetch_sec_filings)

app = mcp.app

