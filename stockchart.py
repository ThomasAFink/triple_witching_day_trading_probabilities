import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date, timedelta

# Reload the data since the environment was reset
OS_PATH = os.path.dirname(os.path.realpath('__file__'))
ticker_symbol = "^GSPC"
gspc_data = pd.read_csv(os.path.join(OS_PATH, f'data/{ticker_symbol}_data_since_1990.csv'))
gspc_data['Date'] = pd.to_datetime(gspc_data['Date'])

# Identify the TWDs (as done previously)
tw_days = gspc_data[gspc_data['Date'].apply(lambda x: x.weekday() == 4 and 15 <= x.day <= 21 and x.month in [3, 6, 9, 12])]

# Filter the data to get the last three years (as done previously)
end_date = gspc_data['Date'].iloc[-1]
start_date = end_date - pd.Timedelta(days=365.25*3)
last_three_years_data = gspc_data[(gspc_data['Date'] >= start_date) & (gspc_data['Date'] <= end_date)]

# Filter TWDs for the last three years (as done previously)
last_three_years_twd = tw_days[(tw_days['Date'] >= start_date) & (tw_days['Date'] <= end_date)]

# Create a daily stock chart for the last three years (as done previously)
fig, ax1 = plt.subplots(figsize=(20, 8))

# Plotting the stock price
ax1.plot(last_three_years_data['Date'], last_three_years_data['Close'], color='b', label='S&P 500 Close Price')
ax1.set_xlabel('Date')
ax1.set_ylabel('S&P 500 Close Price', color='b')
ax1.tick_params('y', colors='b')

# Highlight TWDs
for twd in last_three_years_twd['Date']:
    ax1.axvspan(twd, twd + pd.Timedelta(days=1), color='yellow', alpha=0.3)  # Using shading instead of line for better visibility

# Create a second y-axis to plot volume
ax2 = ax1.twinx()
ax2.bar(last_three_years_data['Date'], last_three_years_data['Volume'], color='gray', alpha=0.3, label='Volume')
ax2.set_ylabel('Volume', color='gray')
ax2.tick_params('y', colors='gray')
ax2.grid(None)

# Title and show plot
plt.title('S&P 500 Daily Close Price and Volume (Last 3 Years)')
fig.tight_layout()
plt.savefig(os.path.join(OS_PATH, f'output/{ticker_symbol}_combined_data_since_1990_stockchart.jpg'), dpi=300)

plt.show()


# Given that we have data up to the end date, let's find the next TWD after the end date
current_date = end_date

# Increment by one day and check if the date meets the TWD criteria. Repeat until we find the next TWD.
while True:
    current_date += timedelta(days=1)
    if current_date.weekday() == 4 and 15 <= current_date.day <= 21 and current_date.month in [3, 6, 9, 12]:
        next_twd = current_date
        break
print(f"Next TWD is on: {next_twd}")