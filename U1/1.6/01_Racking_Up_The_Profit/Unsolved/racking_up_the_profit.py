# """Racking up the profit."""

# Suppose each stock price is the same
stock_price = 30

# But that dividend yields vary across five stocks in your portfolio
dividend_yields = [0.035, 0.040, 0.072, 0.012, 0.052]

# @TODO: Create a variable to hold tallied dividend income
# YOUR CODE HERE!
total_dividend_income = 0

# @TODO: Create a for loop to calculated and add up all the dividend income
# YOUR CODE HERE!
for rate in dividend_yields:
    dividend_income = stock_price * rate
    total_dividend_income = total_dividend_income + dividend_income

# @TODO: Once it's all done, print the dividend income for the entire portfolio
# YOUR CODE HERE!
print("Total Dividends are:", total_dividend_income)


table_data = [
    ["Ticker", "Open", "Close"],
    ["AAPL", 363.25, 363.4],
    ["AMZN", 2756.0, 2757.99],
    ["GOOG", 1409.1, 1408.2]
]

amazon_data = table_data[3]
print(amazon_data)

amazon_data = table_data[2]
amazon_opening_price = amazon_data[1]
print(amazon_opening_price)

for row in table_data:
    ticker = row[0]
    close_px = row[2]
    print(ticker, close_px)


table_data = [
    {
        "Ticker": "AAPL",
        "Open": 363.25,
        "Close": 363.4
    },
    {
        "Ticker": "AMZN",
        "Open": 2756.0,
        "Close": 2757.99
    },
    {
        "Ticker": "GOOG",
        "Open": 1409.1,
        "Close": 1408.2
    }
]
for item in table_data:
    print(item)

for item in table_data:
    ticker = item["Ticker"]
    print(ticker)


from pathlib import Path

csvpath = Path("data.csv")
print(csvpath)
