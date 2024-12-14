import yfinance as yf
import pandas as pd

def fetch_stock_data(symbols, period):
    """
    Fetch stock data for the given symbols and period.
    Args:
        symbols (list): List of stock symbols to fetch.
        period (str): Period to fetch (e.g., '1mo', '3mo', '1y').
    Returns:
        DataFrame: Combined stock data for all symbols.
    """
    try:
        combined_data = []
        for symbol in symbols:
            symbol = symbol.strip()  # Remove whitespace
            stock_data = yf.Ticker(symbol).history(period=period)
            if stock_data.empty:
                print(f"No data found for symbol: {symbol}")
                continue
            stock_data['Symbol'] = symbol
            stock_data = stock_data.reset_index()
            combined_data.append(stock_data)

        if not combined_data:
            raise ValueError("No data fetched for the provided symbols.")
        
        return pd.concat(combined_data, ignore_index=True)
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None
