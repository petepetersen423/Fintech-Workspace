"""Nested Conditionals."""

# @TODO: Create variables with the initial ad price and company type
# YOUR CODE HERE!

ad_price = 10
company_type = "Startup"

# @TODO: Convert the following decision logic into valid Python code.
# if the ad price is affordable (less than 20):

if ad_price < 20:
    #     if the company is a startup:
    if company_type == "Startup":
        #         print that the expected profit is 500
        print("The expected profit is 500")
        #     elif the company is existing:
    elif company_type == "Existing":
        #         print that the expected profit is 100
        print("The expected profit is 100")
        #     else:
    else:
        #         print that the company type is not specified
        print("The company type is noit specified")
# else:
else:
    #     print that the ad price is too expensive
    print("The ad is too expensive!")
