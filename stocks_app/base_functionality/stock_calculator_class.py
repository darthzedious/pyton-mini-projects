class StockCalculator:
    """Class for various stock calculations."""

    @staticmethod
    def calculate_preference_shares_price(div, r):
        return div / r

    @staticmethod
    def calculate_ordinary_shares_price(d1, r, g):
        if r <= g:
            raise ValueError("The required rate of return must be greater than the growth rate.")
        return round(d1 / (r - g), 2)

    @staticmethod
    def return_of_equity(net_profit, equity_capital):
        return round(net_profit / equity_capital, 4)

    @staticmethod
    def calculate_growth_rate_of_dividends(net_profit, equity_capital, ki):
        roe = StockCalculator.return_of_equity(net_profit, equity_capital)
        return round(roe * (1 - ki), 4)