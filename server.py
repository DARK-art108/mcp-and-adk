import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
from html2text import html2text

import uvicorn
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.routing import Route, Mount

from mcp.server.fastmcp import FastMCP
from mcp.shared.exceptions import McpError
from mcp.types import ErrorData, INTERNAL_ERROR, INVALID_PARAMS
from mcp.server.sse import SseServerTransport

mcp = FastMCP("wiki")

@mcp.tool()
def extract_wikipedia_article(url: str) -> str:

    try:
        if not url.startswith("http"):
            raise ValueError("URL must begin with http or https protocol.")

        response = requests.get(url, timeout=8)
        if response.status_code != 200:
            raise McpError(
                ErrorData(
                    code=INTERNAL_ERROR,
                    message=f"Unable to access the article. Server returned status: {response.status_code}"
                )
            )
        soup = BeautifulSoup(response.text, "html.parser")
        content_div = soup.find("div", {"id": "mw-content-text"})
        if not content_div:
            raise McpError(
                ErrorData(
                    code=INVALID_PARAMS,
                    message="The main article content section was not found at the specified Wikipedia URL."
                )
            )
        markdown_text = html2text(str(content_div))
        return markdown_text

    except Exception as e:
        raise McpError(ErrorData(code=INTERNAL_ERROR, message=f"An unexpected error occurred: {str(e)}")) from e

sse = SseServerTransport("/messages/")

async def handle_sse(request: Request) -> None:
    _server = mcp._mcp_server
    async with sse.connect_sse(
        request.scope,
        request.receive,
        request._send,
    ) as (reader, writer):
        await _server.run(reader, writer, _server.create_initialization_options())

app = Starlette(
    debug=True,
    routes=[
        Route("/sse", endpoint=handle_sse),
        Mount("/messages/", app=sse.handle_post_message),
    ],
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8001)