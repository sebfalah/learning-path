import yfinance as yf
import pandas as pd

# Define the ticker symbol for the S&P 500
ticker_symbol = '^GSPC'

# Define the start and end dates
start_date = '2021-01-01'
end_date = '2024-08-06'  # You can use the current date or any specific end date

# Fetch the data
data = yf.download(ticker_symbol, start=start_date, end=end_date)

# Extract only the opening and closing prices
data = data[['Open', 'Close']]

# Save the data to a CSV file
data.to_csv('SP500_daily_data.csv')

print("Data has been successfully downloaded and saved to spx_daily_data.csv")
