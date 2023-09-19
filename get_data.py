import os
import yfinance as yf

OS_PATH = os.path.dirname(os.path.realpath('__file__'))

# Define the ticker symbol
ticker_symbol = "^GSPC"

# Download the historical data
data = yf.download(ticker_symbol, start="1990-01-01")

# Save the data to a CSV file
data.to_csv(os.path.join(OS_PATH, f'data/{ticker_symbol}_data_since_1990.csv'))


print("Data saved to GSPC_data_since_1990.csv")