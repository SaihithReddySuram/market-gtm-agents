import os
import requests
from crewai.tools import tool
from dotenv import load_dotenv

load_dotenv()


@tool("MCP Search Tool")
def mcp_search(query: str) -> str:
    """
    Search the web using the MCP server.

    Input:
        A search query string related to market research,
        competitors, pricing, trends, or customer pain points.

    Returns:
        JSON search results from the MCP server containing:
        - title
        - link
        - snippet
        - source metadata

    Example:
        Query:
            "AI LMS market trends"

        Response:
            {
              "organic_results": [
                {
                  "title": "...",
                  "link": "...",
                  "snippet": "..."
                }
              ]
            }
    """

    response = requests.get(
        "http://127.0.0.1:8000/search",
        params={"query": query},
        timeout=30
    )

    return response.text
