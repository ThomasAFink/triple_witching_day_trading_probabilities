# Triple Witching Day Trading Probabilities

This notebook provides a comprehensive analysis of the S&P 500 Index returns following the Triple Witching Days (TWD) since 1990.

### What is Triple Witching?

Triple Witching refers to the quarterly event in financial markets where stock index futures, stock index options, and stock options all expire on the same day. This event occurs on the third Friday of March, June, September, and December, and is associated with increased trading volume and volatility. The significance of studying the returns after TWD is to understand if any predictable price patterns emerge as a result of this event.

Useful links:

https://www.bloomberg.com/news/articles/2023-09-14/a-4-trillion-triple-witching-event-endangers-stock-market-calm
https://www.investopedia.com/terms/t/triplewitchinghour.asp

Here's the daily stock chart for the S&P 500 over the last three years. The volume is represented by the gray bars, and the Triple Witching Days (TWDs) are highlighted with yellow shading. This visualization should give you a clear view of the price movement and volume, especially around the TWDs.

**stockchart.py**

![image](https://github.com/ThomasAFink/triple_witching_trading_probabilities/blob/main/output/%5EGSPC_combined_data_since_1990_stockchart.jpg?raw=true)

```
Next TWD is on: 2023-12-15 16:00:00 EST
```

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

**Really only the first week following TWD is relevant.**

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

**Average Return:**

The average return for a given period (e.g., one week after TWD) is simply the mean of the returns observed during that period. Mathematically, this is given by:

![image](https://latex.codecogs.com/gif.latex?%5Ctext%7BAverage%20Return%7D%20=%20%5Cfrac%7B1%7D%7Bn%7D%20%5Csum_%7Bi=1%7D%5E%7Bn%7D%20r_i)

Where ![image](https://latex.codecogs.com/gif.latex?r_i) represents the return on the ![image](https://latex.codecogs.com/gif.latex?i%5E%7Bth%7D) day, and ![image](https://latex.codecogs.com/gif.latex?n) is the number of days.

**Standard Deviation of Returns:**
The standard deviation provides a measure of the dispersion of the returns. It's given by:

![image](https://latex.codecogs.com/gif.latex?%5Ctext%7BStandard%20Deviation%7D%20=%20%5Csqrt%7B%5Cfrac%7B1%7D%7Bn-1%7D%20%5Csum_%7Bi=1%7D%5E%7Bn%7D%20(r_i%20-%20%5Cbar%7Br%7D)%5E2%7D)

Where ![image](https://latex.codecogs.com/gif.latex?%5Cbar%7Br%7D) is the average return.


**Probability of the Market Ending Positive:**
This is the probability that the return on a given day is positive. For a set of observations, it's the fraction of days with positive returns:

![image](https://latex.codecogs.com/gif.latex?P(%5Ctext%7BPositive%20Return%7D)%20=%20%5Cfrac%7B%5Ctext%7BNumber%20of%20days%20with%20%7D%20r_i%20%3E%200%7D%7Bn%7D)

**Probability of the Market Ending Negative:**
Similarly, this is the probability that the return on a given day is negative. For a set of observations, it's the fraction of days with negative returns:

![image](https://latex.codecogs.com/gif.latex?P(%5Ctext%7BNegative%20Return%7D)%20=%20%5Cfrac%7B%5Ctext%7BNumber%20of%20days%20with%20%7D%20r_i%20%3C%200%7D%7Bn%7D)

**Bernoulli Trial:**
Consider a single Triple Witching Day. Let's denote the event that the market has a positive return on that day as ![image](https://latex.codecogs.com/gif.latex?X).

Then, ![image](https://latex.codecogs.com/gif.latex?X) can be modeled as a Bernoulli random variable:

![image](https://latex.codecogs.com/gif.latex?X%20=%20%5Cbegin%7Bcases%7D%201%20&%20%5Ctext%7Bif%20market%20has%20a%20positive%20return%20(%22success%22)%7D%20%5C%5C%200%20&%20%5Ctext%7Bif%20market%20does%20not%20have%20a%20positive%20return%20(%22failure%22)%7D%20%5Cend%7Bcases%7D)

The probabilities associated with these outcomes are:

![image](https://latex.codecogs.com/gif.latex?P(X=1)%20=%20p)

![image](https://latex.codecogs.com/gif.latex?P(X=0)%20=%201-p)

**Bernoulli Process:**

Now, let's consider observing the market returns on ![image](https://latex.codecogs.com/gif.latex?n) different Triple Witching Days. Each day is an independent Bernoulli trial. Let's denote the outcome of the market return on the ![image](https://latex.codecogs.com/gif.latex?i%5E%7Bth%7D) day as ![image](https://latex.codecogs.com/gif.latex?X_i).

The sequence (![image](https://latex.codecogs.com/gif.latex?X_1). ![image](https://latex.codecogs.com/gif.latex?X_2),![image](https://latex.codecogs.com/gif.latex?X_3), ... ![image](https://latex.codecogs.com/gif.latex?X_n)) forms a Bernoulli process. Each ![image](https://latex.codecogs.com/gif.latex?X_i) is a Bernoulli random variable:

![image](https://latex.codecogs.com/gif.latex?X_i%20=%20%5Cbegin%7Bcases%7D%201%20&%20%5Ctext%7Bif%20market%20has%20a%20positive%20return%20on%20the%20%7D%20i%5E%7Bth%7D%20%5Ctext%7B%20day%20(%22success%22)%7D%20%5C%5C%200%20&%20%5Ctext%7Bif%20market%20does%20not%20have%20a%20positive%20return%20on%20the%20%7D%20i%5E%7Bth%7D%20%5Ctext%7B%20day%20(%22failure%22)%7D%20%5Cend%7Bcases%7D)

The probabilities remain consistent across the trials:

![image](https://latex.codecogs.com/gif.latex?P(X_i=1)%20=%20p%20%5Cquad%20%5Cforall%20i)

![image](https://latex.codecogs.com/gif.latex?P(X_i=0)%20=%201-p%20%5Cquad%20%5Cforall%20i)

Furthermore, the trials are independent, so for any subset of days ![image](https://latex.codecogs.com/gif.latex?i_1), ![image](https://latex.codecogs.com/gif.latex?i_2), ![image](https://latex.codecogs.com/gif.latex?i_3), ..., ![image](https://latex.codecogs.com/gif.latex?i_k), the joint probability is the product of their individual probabilities:

![image](https://latex.codecogs.com/gif.latex?P(X_%7Bi_1%7D%20=%20x_%7Bi_1%7D,%20X_%7Bi_2%7D%20=%20x_%7Bi_2%7D,%20%5Cdots,%20X_%7Bi_k%7D%20=%20x_%7Bi_k%7D)%20=%20%5Cprod_%7Bj=1%7D%5E%7Bk%7D%20P(X_%7Bi_j%7D%20=%20x_%7Bi_j%7D))

In this Bernoulli process, the total number of "successes" (positive returns) in the ![image](https://latex.codecogs.com/gif.latex?n) trials can be represented as:

![image](https://latex.codecogs.com/gif.latex?S_n%20=%20%5Csum_%7Bi=1%7D%5E%7Bn%7D%20X_i)

This ![image](https://latex.codecogs.com/gif.latex?S_n) follows a binomial distribution with parameters ![image](https://latex.codecogs.com/gif.latex?n) (number of trials) and ![image](https://latex.codecogs.com/gif.latex?p) (probability of success in each trial).







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



Now, even if there's a spike in volume, it doesn't necessarily mean that the price will have a wider range or change. Here's why:

**Consensus in Direction**: If most of the trading volume is biased in one direction (either buying or selling), the price will move primarily in that direction without much volatility. This means high volume but low price range.

**Liquidity and Market Depth**: In highly liquid markets (like the S&P 500), there's always a counterparty available. If there's an increase in buying volume, there might be enough selling interest to absorb it, preventing prices from skyrocketing. Similarly, increased selling might be matched by buying interest. This balance ensures that prices don't fluctuate or change wildly, even if volume is high.

**Nature of TWD**: The transactions on TWD might be more of a function of rolling over positions or offsetting positions rather than initiating new speculative trades. Such activities might increase the volume without causing significant price swings.

Here's the comparison of percentage price ranges and changes (difference between High and Low prices relative to the Low price) for Triple Witching Days (TWD) versus non-TWDs:

<img width="48%" alt="Screenshot 2023-09-20 at 11 18 24" src="https://github.com/ThomasAFink/triple_witching_day_trading_probabilities/assets/53316058/19e92c45-8481-4495-9afb-0bdde4f8d10e">

<img width="48%" alt="Screenshot 2023-09-20 at 11 42 39" src="https://github.com/ThomasAFink/triple_witching_day_trading_probabilities/assets/53316058/0cf81c0e-7594-4aab-bef1-4f5da2079e5a">

![image](https://github.com/ThomasAFink/triple_witching_trading_probabilities/blob/main/output/%5EGSPC_combined_data_since_1990_volume_dist_norm_compare_price.jpg?raw=true)


```
Average Volume on TWDs: 3,490,805,746.27 shares
Average Volume on Non-TWDs: 2,430,337,434.21 shares
Difference in Volume: 1,060,468,312.06 shares
```

### Further Notes

**Liquidity**: The surge in volume on TWD can lead to liquidity effects. Higher liquidity can reduce the bid-ask spread and make it easier for large institutional investors to take or close positions without significantly impacting the price. The immediate aftermath (i.e., the following week) can provide insights into how liquidity is returning to its normal state.

**Market Psychology**: Investors and traders anticipate TWD, and their strategies leading up to this day might be different from their usual approach. Once TWD is over, the subsequent week can show the return to regular trading behavior, and it's essential to understand this transition.

This analysis provides insights into the market behavior following the Triple Witching Days. It's essential to keep in mind that past performance does not guarantee future results, but understanding these patterns can be helpful for investors and traders.

**Note: The aforementioned probabilities are calculated based on historical data and patterns, and while useful, they should be interpreted with caution. Always consider other factors and perform further analysis before making any investment decisions.**
