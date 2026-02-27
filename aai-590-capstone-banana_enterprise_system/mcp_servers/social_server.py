# mcp_servers/social_server.py

from base_mcp import BaseMCP
import requests

mcp = BaseMCP()

def fetch_social_sentiment(ticker: str):
    # Example: Reddit API wrapper
    # Replace with PRAW or Pushshift
    return [f"{ticker} trending positively on investor forums"]

mcp.register("fetch_social_sentiment", fetch_social_sentiment)

app = mcp.app

