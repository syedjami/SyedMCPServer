import os
import sys
from mcp.server.fastmcp import FastMCP

from models.stock_data import StockPriceData


mcp = FastMCP("mcp_server")

# Stock Tool
from stock_service import StockAPIService
@mcp.tool()
def get_stock_info(symbol: str) -> dict:
    """Return the latest price, open price, and previous close for a stock symbol."""
    ss = StockAPIService()
    return ss.get_stock_info(symbol)

def run():
    mcp.run(transport="stdio")

if __name__ == "__main__":
    run()