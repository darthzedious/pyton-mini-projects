import os
from stocks_app.base_functionality.capm_class import FinancialModeling
from stocks_app.base_functionality.stock_calculator_class import StockCalculator
from stocks_app.base_functionality.stock_data_fetcher_class import StockDataFetcher


def main_menu():
    print("\n--- Financial Modeling App ---")
    print("1. Calculate Preference Shares Price")
    print("2. Calculate Ordinary Shares Price")
    print("3. Calculate Return on Equity (ROE)")
    print("4. Calculate Growth Rate of Dividends")
    print("5. Get Fundamental Stock Data")
    print("6. Get Live Stock Price")
    print("7. Get Top 10 Stock Prices")
    print("8. Calculate Beta Coefficient")
    print("9. Calculate Expected Return using CAPM")
    print("10. Plot CAPM Graph")
    print("0. Exit")
    choice = input("Enter your choice: ")
    return choice


def run_app():
    api_key = os.getenv('ALPHA_VANTAGE_API_KEY') # Hides my API key from you
    fetcher = StockDataFetcher(api_key)
    calculator = StockCalculator()

    while True:
        choice = main_menu()

        if choice == '1':
            div = float(input("Enter the dividend of the preference share: "))
            r = float(input("Enter the required rate of return (as a decimal, e.g., 0.08 for 8%): "))
            price = calculator.calculate_preference_shares_price(div, r)
            print(f"Preference Share Price: {price:.2f}")

        elif choice == '2':
            d1 = float(input("Enter the expected dividend in the next period: "))
            r = float(input("Enter the required rate of return (as a decimal, e.g., 0.08 for 8%): "))
            g = float(input("Enter the growth rate of dividends (as a decimal, e.g., 0.02 for 2%): "))
            try:
                price = calculator.calculate_ordinary_shares_price(d1, r, g)
                print(f"Ordinary Share Price: {price:.2f}")
            except ValueError as e:
                print(e)

        elif choice == '3':
            net_profit = float(input("Enter the net profit of the company: "))
            equity_capital = float(input("Enter the equity capital of the company: "))
            roe = calculator.return_of_equity(net_profit, equity_capital)
            print(f"Return on Equity (ROE): {roe:.4f}")

        elif choice == '4':
            net_profit = float(input("Enter the net profit of the company: "))
            equity_capital = float(input("Enter the equity capital of the company: "))
            ki = float(input("Enter the payout ratio (as a decimal, e.g., 0.4 for 40%): "))
            growth_rate = calculator.calculate_growth_rate_of_dividends(net_profit, equity_capital, ki)
            print(f"Growth Rate of Dividends: {growth_rate:.4f}")

        elif choice == '5':
            symbol = input("Enter the stock symbol (e.g., 'AAPL'): ")
            data = fetcher.get_fundamental_stock_data(symbol)
            print(data)

        elif choice == '6':
            symbol = input("Enter the stock symbol (e.g., 'AAPL'): ")
            price = fetcher.get_live_stock_price(symbol)
            print(f"Live Stock Price for {symbol}: {price:.2f}" if price else "Error fetching stock price.")

        elif choice == '7':
            prices = fetcher.get_top_10_stock_prices()
            for symbol, price in prices.items():
                print(f"{symbol}: {price:.2f}")

        elif choice == '8':
            asset_symbol = input("Enter the asset symbol (e.g., 'AAPL'): ")
            market_symbol = input("Enter the market symbol (e.g., '^GSPC' for S&P 500): ")
            start_date = input("Enter the start date (YYYY-MM-DD): ")
            end_date = input("Enter the end date (YYYY-MM-DD): ")
            beta = FinancialModeling.calculate_beta(asset_symbol, market_symbol, start_date, end_date)
            print(f"The Beta coefficient for {asset_symbol} relative to {market_symbol} is {beta:.2f}")

        elif choice == '9':
            rf = float(input("Enter the risk-free rate (as a decimal, e.g., 0.03 for 3%): "))
            beta = float(input("Enter the Beta of the asset: "))
            rm = float(input("Enter the expected market return (as a decimal, e.g., 0.08 for 8%): "))
            expected_return = FinancialModeling.calculate_capm(rf, beta, rm)
            print(f"Expected Return: {expected_return:.2f}")


        elif choice == '10':

            rf = float(input("Enter the risk-free rate (as a decimal, e.g., 0.03 for 3%): "))
            rm = float(input("Enter the expected market return (as a decimal, e.g., 0.08 for 8%): "))
            current_beta = float(input("Enter the current Beta coefficient: "))
            range_offset = float(input("Enter the Beta range offset (e.g., 1.0 for default): "))

            FinancialModeling.plot_capm(rf, rm, current_beta, range_offset)


        elif choice == '0':

            print("Exiting the app. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    run_app()