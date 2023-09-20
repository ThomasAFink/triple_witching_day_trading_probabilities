# Triple Witching Day Trading Probabilities

This Jupyter Notebook code provides a comprehensive analysis of the S&P 500 Index returns following the Triple Witching Days (TWD) since 1990.

### What is Triple Witching?

Triple Witching refers to the quarterly event in financial markets where stock index futures, stock index options, and stock options all expire on the same day. This event occurs on the third Friday of March, June, September, and December, and is associated with increased trading volume and volatility. The significance of studying the returns after TWD is to understand if any predictable price patterns emerge as a result of this event.

https://www.bloomberg.com/news/articles/2023-09-14/a-4-trillion-triple-witching-event-endangers-stock-market-calm
https://www.investopedia.com/terms/t/triplewitchinghour.asp

Here's the daily stock chart for the S&P 500 over the last three years. The volume is represented by the gray bars, and the Triple Witching Days (TWDs) are highlighted with yellow shading. This visualization should give you a clear view of the price movement and volume, especially around the TWDs.

**stockchart.py**

![image](https://github.com/ThomasAFink/triple_witching_trading_probabilities/blob/main/output/%5EGSPC_combined_data_since_1990_stockchart.jpg?raw=true)


#### Identify the TWDs
```
tw_days = gspc_data[gspc_data['Date'].apply(lambda x: x.weekday() == 4 and 15 <= x.day <= 21 and x.month in [3, 6, 9, 12])]
```


1. **Weekday Condition**: Where ```W(d)``` is a function that returns the weekday of date ```d```. The value 4 corresponds to Friday (considering Monday as 0, Tuesday as 1, and so on).
```W(d)=4```


2. **Day of the Month Condition**: Where ```D(d)``` is a function that returns the day of the month for date ```d```.
```15≤D(d)≤21```


3. **Month Condition**: Where ```M(d)``` is a function that returns the month of date ```d```. 
```M(d)∈{3,6,9,12}```


Combining the above conditions, the complete formula to identify a TWD is:
```W(d)=4 AND 15≤D(d)≤21 AND M(d)∈{3,6,9,12}```

In simpler terms, this formula checks if the date ```d``` is a Friday that falls between the 15th and 21st day of the months March, June, September, or December.

### Results

**main.py**

The market tends to have a negative average return in the weeks following the Triple Witching Days, with the third week after TWD seeing the most significant drop of about −0.92%

The volatility (standard deviation) increases with each subsequent week after the TWD which is expected because price changes more over time.
The probability of the market ending positively is lowest in the first week after TWD (only 29.81% and highest in the fourth week (58.33%

Conversely, the probability of the market ending negatively is highest in the first week after TWD (70.19%) and lowest in the fourth week (41.67%).

Really only the first week following TWD is relevant.

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



Now, even if there's a spike in volume (many transactions), it doesn't necessarily mean that the price will have a wider range or change. Here's why:

Consensus in Direction: If most of the trading volume is biased in one direction (either buying or selling), the price will move primarily in that direction without much volatility. This means high volume but low price range.

Liquidity and Market Depth: In highly liquid markets (like the S&P 500), there's always a counterparty available. If there's an increase in buying volume, there might be enough selling interest to absorb it, preventing prices from skyrocketing. Similarly, increased selling might be matched by buying interest. This balance ensures that prices don't fluctuate wildly, even if volume is high.

Nature of TWD: The transactions on TWD might be more of a function of rolling over positions or offsetting positions rather than initiating new speculative trades. Such activities might increase the volume without causing significant price swings.

Here's the comparison of percentage price ranges (difference between High and Low prices relative to the Low price) for Triple Witching Days (TWD) versus non-TWDs:

<img width="46.5%" alt="Screenshot 2023-09-20 at 11 18 24" src="https://github.com/ThomasAFink/triple_witching_trading_probabilities/assets/53316058/063d2406-c214-443b-9e6c-e5e687d56c01">

<img width="46.5%" alt="Screenshot 2023-09-20 at 11 42 39" src="https://github.com/ThomasAFink/triple_witching_trading_probabilities/assets/53316058/2e5ca37d-fffc-44b2-9a72-cb528f36fe37">


![image](https://github.com/ThomasAFink/triple_witching_trading_probabilities/blob/main/output/%5EGSPC_combined_data_since_1990_volume_dist_norm_compare_price.jpg?raw=true)


```
Average Volume on TWDs: 3,490,805,746.27 shares
Average Volume on Non-TWDs: 2,430,337,434.21 shares
Difference in Volume: 1,060,468,312.06 shares
```

### Further Notes

Liquidity: The surge in volume on TWD can lead to liquidity effects. Higher liquidity can reduce the bid-ask spread and make it easier for large institutional investors to take or close positions without significantly impacting the price. The immediate aftermath (i.e., the following week) can provide insights into how liquidity is returning to its normal state.

Market Psychology: Investors and traders anticipate TWD, and their strategies leading up to this day might be different from their usual approach. Once TWD is over, the subsequent week can show the return to regular trading behavior, and it's essential to understand this transition.

This analysis provides insights into the market behavior following the Triple Witching Days. It's essential to keep in mind that past performance does not guarantee future results, but understanding these patterns can be helpful for investors and traders.

**Note: The aforementioned probabilities are calculated based on historical data and patterns, and while useful, they should be interpreted with caution. Always consider other factors and perform further analysis before making any investment decisions.**
