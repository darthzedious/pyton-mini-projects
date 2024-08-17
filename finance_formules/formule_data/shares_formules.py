import os

import requests

def calculate_preference_shares_price(div, r):

    price = div / r
    return price

def calculate_ordinary_shares_price(d1, r, g):
    """
        Calculate the price of ordinary shares using the Gordon Growth Model.

        Args:
            d1 (float): The expected dividend in the next period.
            r (float): The required rate of return (as a decimal, e.g., 0.08 for 8%).
            g (float): The growth rate of dividends (as a decimal, e.g., 0.02 for 2%).

        Returns:
            float: The estimated price of the ordinary share.
        """
    if r <= g:
        raise ValueError("The required rate of return must be greater than the growth rate.")

    price = d1 / (r - g)
    return round(price, 2)

def return_of_equity(net_profit, equity_capital):
    roe = net_profit / equity_capital
    return round(roe, 4)

def calculate_growth_rate_of_dividends(net_profit, equity_capital, ki):
    """
        Calculate the growth rate of dividends using the ROE and payout ratio.

        Args:
            net_profit (float): The net profit of the company.
            equity_capital (float): The equity capital of the company.
            ki (float): The payout ratio (as a decimal, e.g., 0.4 for 40%).

        Returns:
            float: The growth rate of dividends.
        """

    g = return_of_equity(net_profit, equity_capital) * (1 - ki)
    return round(g, 4)


def get_fundamental_stock_data(symbol, api_key):
    """
        Get fundamental stock data for a given symbol.

        Args:
            symbol (str): The stock symbol (e.g., 'AAPL' for Apple).
            api_key (str): Your API key for Alpha Vantage.

        Returns:
            dict: The fundamental stock data.
        """
    url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey={api_key}'
    r = requests.get(url)
    data = r.json()

    if data:
        return data
    else:
        print("Error retrieving data. Please check the symbol or API key.")
        return None


def get_live_stock_price(symbol, api_key):
    """
    Get the live stock price for a given symbol.

    Args:
        symbol (str): The stock symbol (e.g., 'AAPL' for Apple).
        api_key (str): Your API key for Alpha Vantage.

    Returns:
        float: The current stock price, or None if there is an error.
    """
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()

        # Debug: Print the raw response data
        # print("Response JSON:", data)

        # Check if the expected data is in the response
        if "Global Quote" in data and "05. price" in data["Global Quote"]:
            price = float(data["Global Quote"]["05. price"])
            return price
        else:
            print(f"Error: Unexpected data format received for {symbol}. Data: {data}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None

def get_top_10_stock_prices(api_key):
    """Get live prices for the top 10 stocks."""
    top_10_symbols = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'BRK.B', 'NVDA', 'FB', 'JPM', 'JNJ']

    stock_prices = {}
    for symbol in top_10_symbols:
        price = get_live_stock_price(symbol, api_key)
        if price is not None:
            stock_prices[symbol] = price

    return stock_prices


def main():
    api_key = os.getenv('ALPHA_VANTAGE_API_KEY')
    if not api_key:
        raise ValueError("API key not found. Please set the ALPHA_VANTAGE_API_KEY environment variable.")

    prices = get_top_10_stock_prices(api_key)
    for symbol, price in prices.items():
        print(f"The current price of {symbol} is ${price}")

if __name__ == "__main__":
    main()


# def main():
#     api_key = os.getenv('ALPHA_VANTAGE_API_KEY')
#
#     if not api_key:
#         print("API key not found. Please set the ALPHA_VANTAGE_API_KEY environment variable.")
#     else:
#         print(f"API Key: {api_key}")
#
#
# if __name__ == "__main__":
#     main()