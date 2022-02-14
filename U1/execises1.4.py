
# Skill Drill

stock_price = 10.00
estimated_value = 15.00

if stock_price < estimated_value:
    print("Buy this stock because it is on sale!")
else:
    print("Don't buy this stock because it is too expensive right now")

buy_stock = stock_price < estimated_value

print(buy_stock)

is_raining = True

if is_raining:
    print("Don't forget to bring your umbrella.")
else:
    print("You will need your sunglasses today!")

#############################################
# If-Else Statements and Comparison Operators
#############################################
issue_currency = "USD"
price = 30.0

if issue_currency == "USD":
    print("The price is $", price)
else:
    print("The currency is not in USD.")

##########################################
# If-Else Statements and Logical Operators
##########################################

issue_currency = "USD"
price = 30.0

if issue_currency == "USD" and price < 40.0:
    print("The price is $", price)
else:
    print("The currency is not in USD.")

##########################################
# Complex Conditionals - Elif
##########################################

    # Create a variable that identifies currency
issue_currency = "USD"

# Create a variable that identifies price
price = 30.0

# If the currency is USD, print the price. (Don't forget the colon.)
if issue_currency == "USD":
    print("The currency is $", price)

# If the currency is Euro, display the following statement.
elif issue_currency == "EUR":
    print("The currency is €", price)

# If the currency is anything other than USD or Euro, display the following.
else:
    print("The currency is not in USD or EUR.")

##########################################
# Nested Conditions
###########################################

issue_currency = "USD"
price = 30.0

# Check if price is not negative (greater than equal to 0)
if price >= 0:
    # If price is not negative and currency is `USD` (Dollar).
    if issue_currency == "USD":
        print("The currency is $", price)
    # If price is not negative and currency is `EUR` (Euro).
    elif issue_currency == "EUR":
        print("The currency is €", price)
    # If anything other than the above.
    else:
        print("The currency is not in USD or EUR.")
else:
    # If price is negative.
    print("Error, the price listed is a negative number")
