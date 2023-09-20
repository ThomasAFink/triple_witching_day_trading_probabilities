import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

# Load the data for the S&P 500 Index
OS_PATH = os.path.dirname(os.path.realpath('__file__'))
ticker_symbol = "^GSPC"
gspc_data = pd.read_csv(os.path.join(OS_PATH, f'data/{ticker_symbol}_data_since_1990.csv'))
gspc_data['Date'] = pd.to_datetime(gspc_data['Date'])

# Identify the TWDs
tw_days = gspc_data[gspc_data['Date'].apply(lambda x: x.weekday() == 4 and 15 <= x.day <= 21 and x.month in [3, 6, 9, 12])]

# Calculate the average volume on TWDs
avg_volume_twd = tw_days['Volume'].mean()

# Analyzing Volume Around TWD Including the Entire Week and the Week After
full_week_volume_dissipation = []

for date in tw_days['Date']:
    start_date = date - pd.Timedelta(days=4)  # Start 4 days before TWD
    end_date = date + pd.Timedelta(days=8)  # End 8 days after TWD to ensure capturing 5 trading days
    ten_day_data = gspc_data[(gspc_data['Date'] >= start_date) & (gspc_data['Date'] <= end_date)]
    # Ensure we capture 4 days before TWD, the TWD, and the following 5 trading days
    if len(ten_day_data) == 10:
        full_week_volume_dissipation.append(ten_day_data['Volume'].values)

# Calculate the average volume for each of the 10 days
avg_full_week_volume_dissipation = np.mean(full_week_volume_dissipation, axis=0)

# Plot the average volume over the 10-day period
days_full_week = ['Day -4', 'Day -3', 'Day -2', 'Day -1', 'TWD', 'Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5']
plt.figure(figsize=(12, 6))
plt.plot(days_full_week, avg_full_week_volume_dissipation, marker='o', color='b', label='Average Volume Around TWD')
plt.axhline(avg_volume_twd, color='r', linestyle='--', label='Average Volume on TWD')
plt.xlabel('Days Around TWD')
plt.ylabel('Volume')
plt.title('Volume Around TWD Including the Entire Week and the Week After')
plt.legend()
plt.grid(True)
plt.savefig(os.path.join(OS_PATH, f'output/{ticker_symbol}_combined_data_since_1990_volume.jpg'), dpi=300)
plt.show()

# Plotting the distribution of volumes on all TWDs without saving
plt.figure(figsize=(12, 6))
plt.hist(tw_days['Volume'], bins=30, color='b', alpha=0.7, label='Volume Distribution on TWDs')
plt.axvline(avg_volume_twd, color='r', linestyle='--', label='Average Volume on TWDs')
plt.xlabel('Volume')
plt.ylabel('Frequency')
plt.title('Volume Distribution on Triple Witching Days Since 1990')
plt.legend()
plt.grid(True)
plt.savefig(os.path.join(OS_PATH, f'output/{ticker_symbol}_combined_data_since_1990_volume_dist.jpg'), dpi=300)
plt.show()

# Recalculate the average volume on non-TWDs
non_twd_data = gspc_data.drop(tw_days.index)
avg_volume_non_twd = non_twd_data['Volume'].mean()

# Calculate parameters for TWD volume
mean_volume_twd = tw_days['Volume'].mean()
std_volume_twd = tw_days['Volume'].std()

# Calculate parameters for non-TWD volume
mean_volume_non_twd = non_twd_data['Volume'].mean()
std_volume_non_twd = non_twd_data['Volume'].std()

# Generate a range of volume values for plotting
x_twd = np.linspace(mean_volume_twd - 4*std_volume_twd, mean_volume_twd + 4*std_volume_twd, 1000)
x_non_twd = np.linspace(mean_volume_non_twd - 4*std_volume_non_twd, mean_volume_non_twd + 4*std_volume_non_twd, 1000)

# Generate normal distribution curves for both sets of volume values
pdf_twd = stats.norm.pdf(x_twd, mean_volume_twd, std_volume_twd)
pdf_non_twd = stats.norm.pdf(x_non_twd, mean_volume_non_twd, std_volume_non_twd)

# Plot histograms and normal distribution curves
# Plot histograms, normal distribution curves, and dashed vertical lines for means with updated labels

plt.figure(figsize=(14, 7))
plt.hist(tw_days['Volume'], bins=30, density=True, color='b', alpha=0.5, 
         label=f'TWD Volume Histogram (µ: {mean_volume_twd:,.2f})')
plt.hist(non_twd_data['Volume'], bins=30, density=True, color='g', alpha=0.5, 
         label=f'Non-TWD Volume Histogram (µ: {mean_volume_non_twd:,.2f})')
plt.plot(x_twd, pdf_twd, 'b-', 
         label=f'TWD Normal Distribution (σ: {std_volume_twd:,.2f})')
plt.plot(x_non_twd, pdf_non_twd, 'g-', 
         label=f'Non-TWD Normal Distribution (σ: {std_volume_non_twd:,.2f})')

# Add dashed vertical lines for the means
plt.axvline(mean_volume_twd, color='b', linestyle='--', alpha=0.7)
plt.axvline(mean_volume_non_twd, color='g', linestyle='--', alpha=0.7)

plt.xlabel('Volume')
plt.ylabel('Density')
plt.title('Volume Distribution for TWD vs. Non-TWD with Statistics and Means')
plt.legend()
plt.grid(True)
plt.savefig(os.path.join(OS_PATH, f'output/{ticker_symbol}_combined_data_since_1990_volume_dist_norm_compare.jpg'), dpi=300)
plt.show()

# Calculate percentage price ranges for TWDs and non-TWDs (as done previously)
tw_days['Price Range %'] = ((tw_days['High'] - tw_days['Low']) / tw_days['Low']) * 100
non_twd_data['Price Range %'] = ((non_twd_data['High'] - non_twd_data['Low']) / non_twd_data['Low']) * 100

# Parameters for TWD price range percentage
mean_range_pct_twd = tw_days['Price Range %'].mean()
std_range_pct_twd = tw_days['Price Range %'].std()

# Parameters for non-TWD price range percentage
mean_range_pct_non_twd = non_twd_data['Price Range %'].mean()
std_range_pct_non_twd = non_twd_data['Price Range %'].std()

# Range of price range percentage values for plotting
x_range_pct_twd = np.linspace(mean_range_pct_twd - 4*std_range_pct_twd, mean_range_pct_twd + 4*std_range_pct_twd, 1000)
x_range_pct_non_twd = np.linspace(mean_range_pct_non_twd - 4*std_range_pct_non_twd, mean_range_pct_non_twd + 4*std_range_pct_non_twd, 1000)

# Normal distribution curves for both sets of price range percentage values
pdf_range_pct_twd = stats.norm.pdf(x_range_pct_twd, mean_range_pct_twd, std_range_pct_twd)
pdf_range_pct_non_twd = stats.norm.pdf(x_range_pct_non_twd, mean_range_pct_non_twd, std_range_pct_non_twd)


# Calculate percentage price changes for TWDs and non-TWDs
tw_days['Price Change %'] = ((tw_days['Close'] - tw_days['Open']) / tw_days['Open']) * 100
non_twd_data['Price Change %'] = ((non_twd_data['Close'] - non_twd_data['Open']) / non_twd_data['Open']) * 100

# Calculate parameters for TWD price change percentage (as done previously)
mean_change_pct_twd = tw_days['Price Change %'].mean()
std_change_pct_twd = tw_days['Price Change %'].std()

# Calculate parameters for non-TWD price change percentage (as done previously)
mean_change_pct_non_twd = non_twd_data['Price Change %'].mean()
std_change_pct_non_twd = non_twd_data['Price Change %'].std()

# Generate a range of price change percentage values for plotting (as done previously)
x_change_pct_twd = np.linspace(mean_change_pct_twd - 4*std_change_pct_twd, mean_change_pct_twd + 4*std_change_pct_twd, 1000)
x_change_pct_non_twd = np.linspace(mean_change_pct_non_twd - 4*std_change_pct_non_twd, mean_change_pct_non_twd + 4*std_change_pct_non_twd, 1000)

# Generate normal distribution curves for both sets of price change percentage values (as done previously)
pdf_change_pct_twd = stats.norm.pdf(x_change_pct_twd, mean_change_pct_twd, std_change_pct_twd)
pdf_change_pct_non_twd = stats.norm.pdf(x_change_pct_non_twd, mean_change_pct_non_twd, std_change_pct_non_twd)


# Create a figure with two subplots side by side
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(18, 7))

# Plotting Price Range Percentage
axes[0].hist(tw_days['Price Range %'], bins=30, density=True, color='b', alpha=0.5, 
             label=f'TWD Price Range % Histogram (Mean: {mean_range_pct_twd:.2f}%)')
axes[0].hist(non_twd_data['Price Range %'], bins=30, density=True, color='g', alpha=0.5, 
             label=f'Non-TWD Price Range % Histogram (Mean: {mean_range_pct_non_twd:.2f}%)')
axes[0].plot(x_range_pct_twd, pdf_range_pct_twd, 'b-', 
             label=f'TWD Normal Distribution (µ: {mean_range_pct_twd:.2f}%, σ: {std_range_pct_twd:.2f}%)')
axes[0].plot(x_range_pct_non_twd, pdf_range_pct_non_twd, 'g-', 
             label=f'Non-TWD Normal Distribution (µ: {mean_range_pct_non_twd:.2f}%, σ: {std_range_pct_non_twd:.2f}%)')
axes[0].axvline(mean_range_pct_twd, color='b', linestyle='--', alpha=0.7)
axes[0].axvline(mean_range_pct_non_twd, color='g', linestyle='--', alpha=0.7)
axes[0].set_xlabel('Price Range Percentage (High - Low) / Low')
axes[0].set_ylabel('Density')
axes[0].set_title('Price Range Percentage Distribution')
axes[0].legend()
axes[0].grid(True)

# Plotting Price Change Percentage
axes[1].hist(tw_days['Price Change %'], bins=30, density=True, color='b', alpha=0.5, 
             label=f'TWD Price Change % Histogram (Mean: {mean_change_pct_twd:.2f}%)')
axes[1].hist(non_twd_data['Price Change %'], bins=30, density=True, color='g', alpha=0.5, 
             label=f'Non-TWD Price Change % Histogram (Mean: {mean_change_pct_non_twd:.2f}%)')
axes[1].plot(x_change_pct_twd, pdf_change_pct_twd, 'b-', 
             label=f'TWD Normal Distribution (µ: {mean_change_pct_twd:.2f}%, σ: {std_change_pct_twd:.2f}%)')
axes[1].plot(x_change_pct_non_twd, pdf_change_pct_non_twd, 'g-', 
             label=f'Non-TWD Normal Distribution (µ: {mean_change_pct_non_twd:.2f}%, σ: {std_change_pct_non_twd:.2f}%)')
axes[1].axvline(mean_change_pct_twd, color='b', linestyle='--', alpha=0.7)
axes[1].axvline(mean_change_pct_non_twd, color='g', linestyle='--', alpha=0.7)
axes[1].set_xlabel('Price Change Percentage (Close - Open) / Open')
axes[1].set_ylabel('Density')
axes[1].set_title('Price Change Percentage Distribution')
axes[1].legend()
axes[1].grid(True)

plt.tight_layout()
plt.savefig(os.path.join(OS_PATH, f'output/{ticker_symbol}_combined_data_since_1990_volume_dist_norm_compare_price.jpg'), dpi=300)
plt.show()



print("Summary Volume Statistics for the S&P 500 Index Around Triple Witching Days Since 1990")
print("-------------------------------------------------------------------------------------------------")
print(f"Average Volume on TWDs: {avg_volume_twd:,.2f} shares")
print(f"Average Volume on Non-TWDs: {avg_volume_non_twd:,.2f} shares")
print(f"Difference in Volume: {avg_volume_twd - avg_volume_non_twd:,.2f} shares")
print("-------------------------------------------------------------------------------------------------")
