from dataclasses import dataclass


@dataclass
class StockPriceData:
    symbol: str
    latest_price: float
    open_price: float
    previous_close: float

    # def __init__(self, symbol: str, latest_price: float, open_price: float, previous_close: float):
    #     self.symbol = symbol
    #     self.latest_price = latest_price
    #     self.open_price = open_price
    #     self.previous_close = previous_close

    # def to_dict(self):
    #     return {
    #         "symbol": self.symbol,
    #         "latest_price": self.latest_price,
    #         "open_price": self.open_price,
    #         "previous_close": self.previous_close,
    #     }