import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

def calculate_n_week_return(date, data, n):
    start_date = date + pd.Timedelta(days=1)
    end_date = start_date + pd.Timedelta(days=7*n)
    n_week_data = data[(data['Date'] >= start_date) & (data['Date'] <= end_date)]
    if len(n_week_data) != 5*n:
        return None
    n_week_return = (n_week_data.iloc[-1]['Close'] - n_week_data.iloc[0]['Open']) / n_week_data.iloc[0]['Open']
    return n_week_return

OS_PATH = os.path.dirname(os.path.realpath('__file__'))
ticker_symbol = "^GSPC"
gspc_data = pd.read_csv(os.path.join(OS_PATH, f'data/{ticker_symbol}_data_since_1990.csv'))
gspc_data['Date'] = pd.to_datetime(gspc_data['Date'])
tw_days = gspc_data[gspc_data['Date'].apply(lambda x: x.weekday() == 4 and 15 <= x.day <= 21 and x.month in [3, 6, 9, 12])]

weeks_to_examine = [1, 2, 3, 4]
week_labels = ["One", "Two", "Three", "Four"]
returns = {}

plt.figure(figsize=(14, 8))

for i, n in enumerate(weeks_to_examine):
    tw_days[f'{n}_Week_Return'] = tw_days['Date'].apply(lambda x: calculate_n_week_return(x, gspc_data, n))
    tw_days_clean = tw_days.dropna(subset=[f'{n}_Week_Return'])
    returns[n] = tw_days_clean[f'{n}_Week_Return'].values * 100

    average_return_percentage = tw_days_clean[f'{n}_Week_Return'].mean() * 100
    std_return_percentage = tw_days_clean[f'{n}_Week_Return'].std() * 100

    x_corrected_percentage = np.linspace(average_return_percentage - 4*std_return_percentage, average_return_percentage + 4*std_return_percentage, 100)
    pdf_corrected_percentage = stats.norm.pdf(x_corrected_percentage, average_return_percentage, std_return_percentage)
    
    bin_width = (max(returns[n]) - min(returns[n])) / 20
    scaled_pdf = pdf_corrected_percentage * len(returns[n]) * bin_width

    plt.subplot(2, 2, i+1)
    plt.hist(returns[n], bins=20, alpha=0.6, color='b', label=f"Histogram {week_labels[i]} Week Returns")
    plt.plot(x_corrected_percentage, scaled_pdf, 'k', linewidth=2, label=f"Normal Distribution {week_labels[i]} Week Returns")
    
    title_percentage = f"Fit results: µ = {average_return_percentage:.2f}%, std = {std_return_percentage:.2f}%"
    plt.title(title_percentage)
    
    plt.xlabel("Return (%)")
    plt.ylabel("Frequency")
    plt.legend()
    plt.grid(True)

plt.tight_layout()
plt.savefig(os.path.join(OS_PATH, f'output/{ticker_symbol}_combined_data_since_1990.jpg'), dpi=300)
plt.show()

plt.tight_layout()
plt.savefig(os.path.join(OS_PATH, f'output/{ticker_symbol}_combined_data_since_1990.jpg'), dpi=300)
plt.show()

print("------------------------------------------------------------------------------------------------------------------------")
print("Summary Statistics for the S&P 500 Index Following Triple Witching Days Since 1990")
for i, n in enumerate(weeks_to_examine):
    tw_days_clean = tw_days.dropna(subset=[f'{n}_Week_Return'])
    
    avg_return = tw_days_clean[f'{n}_Week_Return'].mean() * 100
    std_return = tw_days_clean[f'{n}_Week_Return'].std() * 100
    prob_positive = (tw_days_clean[f'{n}_Week_Return'] > 0).mean() * 100
    prob_negative = (tw_days_clean[f'{n}_Week_Return'] < 0).mean() * 100

    print(f"\n{week_labels[i]} Week After TWD:")
    print(f"Average Return: {avg_return:.4f}%")
    print(f"Standard Deviation of Returns: {std_return:.4f}%")
    print(f"Probability of the Market Ending Positive: {prob_positive:.2f}%")
    print(f"Probability of the Market Ending Negative: {prob_negative:.2f}%")
