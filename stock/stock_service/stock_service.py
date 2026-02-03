import yfinance as yf
from dataclasses import dataclass,asdict

from models.stock_data import StockPriceData

class StockAPIService:
    def get_stock_info(self, symbol: str) -> dict:
        """
        Return the latest price, open price, and previous close for a stock symbol.
        Example: AAPL, MSFT, TSLA
        """

        ticker = yf.Ticker(symbol)
        data = ticker.history(period="1d")

        if data.empty:
            return f"Could not fetch data for {symbol}. It may be an invalid ticker."

        latest = data.iloc[-1]

        price = latest["Close"]
        open_price = latest["Open"]
        prev_close = latest["Close"]  # Yahoo Finance gives only today's data in 1d mode

        response = StockPriceData(symbol, price, open_price, prev_close)
        return asdict(response)

        # return (
        #     f"Stock: {symbol}\n"
        #     f"Current Price: ${price:.2f}\n"
        #     f"Open Price: ${open_price:.2f}\n"
        #     f"Previous Close: ${prev_close:.2f}"
        # )

