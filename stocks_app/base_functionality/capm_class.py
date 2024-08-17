import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf


class FinancialModeling:
    @staticmethod
    def calculate_beta(asset_symbol, market_symbol, start_date, end_date):
        """
            Calculate the Beta coefficient of an asset relative to a market index.

            Args:
                asset_symbol (str): Symbol for the asset (e.g., 'AAPL').
                market_symbol (str): Symbol for the market index (e.g., 'S&P500').
                start_date (str): Start date for historical data (e.g., '2020-01-01').
                end_date (str): End date for historical data (e.g., '2023-01-01').

            Returns:
                float: Beta coefficient of the asset.
            """
        asset_data = yf.download(asset_symbol, start=start_date, end=end_date)['Adj Close']
        market_data = yf.download(market_symbol, start=start_date, end=end_date)['Adj Close']
        asset_returns = asset_data.pct_change().dropna()
        market_returns = market_data.pct_change().dropna()
        covariance_matrix = np.cov(asset_returns, market_returns)
        beta = covariance_matrix[0, 1] / covariance_matrix[1, 1]
        return beta

    @staticmethod
    def calculate_capm(rf, beta, rm):
        """
            Calculate the expected return of an asset using the Capital Asset Pricing Model (CAPM).

            Args:
                rf (float): Risk-free rate (e.g., 0.03 for 3%).
                beta (float): Beta of the asset (e.g., 1.2).
                rm (float): Expected market return (e.g., 0.08 for 8%).

            Returns:
                float: Expected return of the asset.
            """
        expected_asset_return = rf + beta * (rm - rf)
        return expected_asset_return

    @staticmethod
    def plot_capm(rf, rm, current_beta, range_offset=1.0):
        """
            Plot the Capital Asset Pricing Model (CAPM) graph.

            Args:
                rf (float): Risk-free rate.
                rm (float): Expected market return.
                current_beta (float): Current Beta coefficient for context.
                range_offset (float): Offset to extend the Beta range beyond the current Beta.
            """
        beta_range = (0, current_beta + range_offset)
        beta_values = np.linspace(beta_range[0], beta_range[1], 100)
        expected_returns = [FinancialModeling.calculate_capm(rf, beta, rm) for beta in beta_values]
        current_expected_return = FinancialModeling.calculate_capm(rf, current_beta, rm)

        plt.figure(figsize=(12, 8))
        plt.plot(beta_values, expected_returns, label='CAPM Line', color='b')
        plt.axvline(x=current_beta, color='r', linestyle='--', label=f'Current Beta ({current_beta})')
        plt.scatter(current_beta, current_expected_return, color='g', zorder=5)

        plt.annotate(
            f'{current_expected_return:.2f}',
            xy=(current_beta, current_expected_return),
            xytext=(current_beta + 0.5, current_expected_return + 0.01),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=12,
            color='black'
        )

        plt.title('CAPM: Expected Return vs Beta')
        plt.xlabel('Beta (β)')
        plt.ylabel('Expected Return')
        plt.grid(True)
        plt.legend()
        plt.show()