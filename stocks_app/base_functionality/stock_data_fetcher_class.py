from tkinter import messagebox
import requests


class StockDataFetcher:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_fundamental_stock_data(self, symbol):
        """
                Get fundamental stock data for a given symbol.

                Args:
                    symbol (str): The stock symbol (e.g., 'AAPL' for Apple).

                Returns:
                    dict: The fundamental stock data.
                """

        url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey={self.api_key}'
        r = requests.get(url)
        data = r.json()
        if data:
            return data
        else:
            messagebox.showerror("Error", "Error retrieving data. Please check the symbol or API key.")
            return None

    def get_live_stock_price(self, symbol):
        """
            Get the live stock price for a given symbol.

            Args:
                symbol (str): The stock symbol (e.g., 'AAPL' for Apple).

            Returns:
                float: The current stock price.
            """
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={self.api_key}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if "Global Quote" in data and "05. price" in data["Global Quote"]:
                return float(data["Global Quote"]["05. price"])
            else:
                messagebox.showerror("Error", f"Unexpected data format received for {symbol}.")
                return None
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Request error: {e}")
            return None

    def get_top_10_stock_prices(self):
        """Get live prices for the top 10 stocks."""

        top_10_symbols = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'BRK.B', 'NVDA', 'META', 'JPM', 'JNJ']
        stock_prices = {}
        for symbol in top_10_symbols:
            price = self.get_live_stock_price(symbol)
            if price is not None:
                stock_prices[symbol] = price
        return stock_prices