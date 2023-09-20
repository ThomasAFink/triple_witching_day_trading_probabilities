# Triple Witching Trading Probabilities

This Jupyter Notebook code provides a comprehensive analysis of the S&P 500 Index returns following the Triple Witching Days (TWD) since 1990.

### What is Triple Witching?

Triple Witching refers to the quarterly event in financial markets where stock index futures, stock index options, and stock options all expire on the same day. This event occurs on the third Friday of March, June, September, and December, and is associated with increased trading volume and volatility. The significance of studying the returns after TWD is to understand if any predictable price patterns emerge as a result of this event.


### Results

**main.py**

![image](https://github.com/ThomasAFink/triple_witching_trading_probabilities/blob/main/output/%5EGSPC_combined_data_since_1990.jpg?raw=true)

```
One Week After TWD:
Average Return: −0.4154%
Standard Deviation of Returns: 2.3792%
Probability of the Market Ending Positive: 29.81%
Probability of the Market Ending Negative: 70.19%

Two Weeks After TWD:
Average Return: -0.0212%
Standard Deviation of Returns: 3.5441%
Probability of the Market Ending Positive: 51.39%
Probability of the Market Ending Negative: 48.61%

Three Weeks After TWD:
Average Return: -0.9205
Standard Deviation of Returns: 5.3904%
Probability of the Market Ending Positive: 42.22%
Probability of the Market Ending Negative: 57.78%

Four Weeks After TWD:
Average Return: −0.5063%
Standard Deviation of Returns: 5.8430%
Probability of the Market Ending Positive: 58.33%
Probability of the Market Ending Negative: 41.67%
```

**volume.py**

Here's the volume visualization for the Triple Witching Days (TWD) since 1990.

The extended plot encapsulates the entire trading week of the Triple Witching Day (TWD) as well as the week after. After the TWD, there's a noticeable drop in trading volume on the first day.

![image](https://github.com/ThomasAFink/triple_witching_trading_probabilities/blob/main/output/%5EGSPC_combined_data_since_1990_volume.jpg?raw=true)

The histogram displays the distribution of volumes on all TWDs, providing a visual representation of the spread and central tendency of the volume on these days. The red dashed line represents the average volume on TWDs.

![image](https://github.com/ThomasAFink/triple_witching_trading_probabilities/blob/main/output/%5EGSPC_combined_data_since_1990_volume_dist.jpg?raw=true)

The histograms depict the actual distributions of trading volumes for TWDs (in blue) and non-TWDs (in green).
The solid lines represent the corresponding normal distributions based on the mean and standard deviation of the volumes for each group.

Key Observation: The volume on TWDs tends to be higher, with the peak of its distribution shifted to the right compared to the non-TWD distribution.

![image](https://github.com/ThomasAFink/triple_witching_trading_probabilities/blob/main/output/%5EGSPC_combined_data_since_1990_volume_dist_norm_compare.jpg?raw=true)

```
Average Volume on TWDs: 3,490,805,746.27 shares
Average Volume on Non-TWDs: 2,430,337,434.21 shares
Difference in Volume: 1,060,468,312.06 shares
```

### Observations:

The market tends to have a negative average return in the weeks following the Triple Witching Days, with the third week after TWD seeing the most significant drop of about −0.92%

The volatility (standard deviation) increases with each subsequent week after the TWD which is expected because price changes more over time.
The probability of the market ending positively is lowest in the first week after TWD (only 29.81% and highest in the fourth week (58.33%

Conversely, the probability of the market ending negatively is highest in the first week after TWD (70.19%) and lowest in the fourth week (41.67%).

This analysis provides insights into the market behavior following the Triple Witching Days. It's essential to keep in mind that past performance does not guarantee future results, but understanding these patterns can be helpful for investors and traders.

**Note: The aforementioned probabilities are calculated based on historical data and patterns, and while useful, they should be interpreted with caution. Always consider other factors and perform further analysis before making any investment decisions.**
