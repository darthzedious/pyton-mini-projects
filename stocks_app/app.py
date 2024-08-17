import os
import tkinter as tk
from tkinter import ttk, messagebox
from stocks_app.base_functionality.capm_class import FinancialModeling
from stocks_app.base_functionality.stock_calculator_class import StockCalculator
from stocks_app.base_functionality.stock_data_fetcher_class import StockDataFetcher


class FinancialApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Financial Modeling App")
        self.geometry("600x500")
        self.api_key = os.getenv('ALPHA_VANTAGE_API_KEY')  # Hides my API key from you
        self.fetcher = StockDataFetcher(self.api_key)

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Choose an operation:", font=('Arial', 14)).pack(pady=10)

        ttk.Button(self, text="Calculate Preference Shares Price", command=self.calculate_preference_shares_price).pack(pady=5, fill='x')
        ttk.Button(self, text="Calculate Ordinary Shares Price", command=self.calculate_ordinary_shares_price).pack(pady=5, fill='x')
        ttk.Button(self, text="Calculate Return on Equity (ROE)", command=self.calculate_roe).pack(pady=5, fill='x')
        ttk.Button(self, text="Calculate Growth Rate of Dividends", command=self.calculate_growth_rate_of_dividends).pack(pady=5, fill='x')
        ttk.Button(self, text="Get Fundamental Stock Data", command=self.get_fundamental_stock_data).pack(pady=5, fill='x')
        ttk.Button(self, text="Get Live Stock Price", command=self.get_live_stock_price).pack(pady=5, fill='x')
        ttk.Button(self, text="Get Top 10 Stock Prices", command=self.get_top_10_stock_prices).pack(pady=5, fill='x')
        ttk.Button(self, text="Calculate Beta Coefficient", command=self.calculate_beta).pack(pady=5, fill='x')
        ttk.Button(self, text="Calculate Expected Return using CAPM", command=self.calculate_capm).pack(pady=5, fill='x')
        ttk.Button(self, text="Plot CAPM Graph", command=self.plot_capm).pack(pady=5, fill='x')

    def calculate_preference_shares_price(self):
        div = self.get_float_input("Enter the dividend of the preference share: ")
        r = self.get_float_input("Enter the required rate of return (as a decimal, e.g., 0.08 for 8%): ")
        if div is not None and r is not None:
            price = StockCalculator.calculate_preference_shares_price(div, r)
            messagebox.showinfo("Result", f"Preference Share Price: {price:.2f}")

    def calculate_ordinary_shares_price(self):
        d1 = self.get_float_input("Enter the expected dividend in the next period: ")
        r = self.get_float_input("Enter the required rate of return (as a decimal, e.g., 0.08 for 8%): ")
        g = self.get_float_input("Enter the growth rate of dividends (as a decimal, e.g., 0.02 for 2%): ")
        if d1 is not None and r is not None and g is not None:
            try:
                price = StockCalculator.calculate_ordinary_shares_price(d1, r, g)
                messagebox.showinfo("Result", f"Ordinary Share Price: {price:.2f}")
            except ValueError as e:
                messagebox.showerror("Error", str(e))

    def calculate_roe(self):
        net_profit = self.get_float_input("Enter the net profit of the company: ")
        equity_capital = self.get_float_input("Enter the equity capital of the company: ")
        if net_profit is not None and equity_capital is not None:
            roe = StockCalculator.return_of_equity(net_profit, equity_capital)
            messagebox.showinfo("Result", f"Return on Equity (ROE): {roe:.4f}")

    def calculate_growth_rate_of_dividends(self):
        net_profit = self.get_float_input("Enter the net profit of the company: ")
        equity_capital = self.get_float_input("Enter the equity capital of the company: ")
        ki = self.get_float_input("Enter the payout ratio (as a decimal, e.g., 0.4 for 40%): ")
        if net_profit is not None and equity_capital is not None and ki is not None:
            growth_rate = StockCalculator.calculate_growth_rate_of_dividends(net_profit, equity_capital, ki)
            messagebox.showinfo("Result", f"Growth Rate of Dividends: {growth_rate:.4f}")

    def get_fundamental_stock_data(self):
        symbol = self.get_string_input("Enter the stock symbol (e.g., 'AAPL'): ")
        if symbol:
            data = self.fetcher.get_fundamental_stock_data(symbol)
            if data:
                info = "\n".join(f"{key}: {value}" for key, value in data.items())
                self.show_text("Fundamental Stock Data", info)

    def get_live_stock_price(self):
        symbol = self.get_string_input("Enter the stock symbol (e.g., 'AAPL'): ")
        if symbol:
            price = self.fetcher.get_live_stock_price(symbol)
            if price is not None:
                messagebox.showinfo("Result", f"Live Stock Price: {price:.2f}")

    def get_top_10_stock_prices(self):
        prices = self.fetcher.get_top_10_stock_prices()
        if prices:
            info = "\n".join(f"{symbol}: {price:.2f}" for symbol, price in prices.items())
            self.show_text("Top 10 Stock Prices", info)

    def calculate_beta(self):
        asset_symbol = self.get_string_input("Enter the asset symbol (e.g., 'AAPL'): ")
        market_symbol = self.get_string_input("Enter the market symbol (e.g., '^GSPC'): ")
        start_date = self.get_string_input("Enter the start date (e.g., '2020-01-01'): ")
        end_date = self.get_string_input("Enter the end date (e.g., '2023-01-01'): ")
        if asset_symbol and market_symbol and start_date and end_date:
            beta = FinancialModeling.calculate_beta(asset_symbol, market_symbol, start_date, end_date)
            messagebox.showinfo("Result", f"Beta coefficient: {beta:.2f}")

    def calculate_capm(self):
        rf = self.get_float_input("Enter the risk-free rate (as a decimal, e.g., 0.03 for 3%): ")
        beta = self.get_float_input("Enter the Beta coefficient (e.g., 1.2): ")
        rm = self.get_float_input("Enter the expected market return (as a decimal, e.g., 0.08 for 8%): ")
        if rf is not None and beta is not None and rm is not None:
            expected_return = FinancialModeling.calculate_capm(rf, beta, rm)
            messagebox.showinfo("Result", f"Expected Return: {expected_return:.2f}")

    def plot_capm(self):
        rf = self.get_float_input("Enter the risk-free rate (as a decimal, e.g., 0.03 for 3%): ")
        rm = self.get_float_input("Enter the expected market return (as a decimal, e.g., 0.08 for 8%): ")
        current_beta = self.get_float_input("Enter the current Beta coefficient: ")
        range_offset = self.get_float_input("Enter the Beta range offset (e.g., 1.0 for default): ")
        if rf is not None and rm is not None and current_beta is not None and range_offset is not None:
            FinancialModeling.plot_capm(rf, rm, current_beta, range_offset)

    def get_float_input(self, prompt):
        value = self.get_input(prompt)
        try:
            return float(value)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number.")
            return None

    def get_string_input(self, prompt):
        return self.get_input(prompt)

    def get_input(self, prompt):
        input_dialog = tk.Toplevel(self)
        input_dialog.title("Input")
        tk.Label(input_dialog, text=prompt).pack(pady=10)
        entry_value = tk.StringVar()
        entry = tk.Entry(input_dialog, textvariable=entry_value)
        entry.pack(pady=5)
        tk.Button(input_dialog, text="Submit", command=input_dialog.destroy).pack(pady=10)
        self.wait_window(input_dialog)
        return entry_value.get()

    def show_text(self, title, text):
        text_dialog = tk.Toplevel(self)
        text_dialog.title(title)
        tk.Label(text_dialog, text=text, padx=10, pady=10).pack()
        tk.Button(text_dialog, text="Close", command=text_dialog.destroy).pack(pady=10)

if __name__ == "__main__":
    app = FinancialApp()
    app.mainloop()