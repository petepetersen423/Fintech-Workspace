import csv
from pathlib import Path

equity_funding = [
    {"Company": "CryptoVisors", "Amount": 200000, "Series": "A"},
    {"Company": "Flutterwave", "Amount": 65000000, "Series": "D"},
    {"Company": "nCino", "Amount": 80000000, "Series": "D"},
    {"Company": "Privacy.com", "Amount": 10000000, "Series": "B"},
]

# Create an empty list called `big_raisers`
# YOUR CODE HERE!

big_raisers = []

# Iterate (loop) through each dictionary in the list of dictionaries.
for equity in equity_funding:
    # @TODO: Inside of the `for` loop, write an `if` statement that
    # appends the dictionary to the `big_raisers` list
    # if the funding amount is greater than $50 million (50000000).
    # YOUR CODE HERE!
    if equity["Amount"] > 50000000:
        big_raisers.append(equity)
print(big_raisers)


# Set the output header
header = ["Company", "Amount", "Series"]

# @TODO: Create a Path to a new CSV file
# YOUR CODE HERE!

csvfile = Path("big_raisers.csv")

print("Writing the data to a CSV file...")
# @TODO: Open the output CSV file path using `with open`
# YOUR CODE HERE!
csvpath = Path("my_output.csv")

with open(csvpath, 'w', newline='') as csvfile:
    # @TODO: Create a csvwriter
    # YOUR CODE HERE!
    csvwriter = csv.writer(csvfile)
    # Write the header to the CSV file
    header = ["Company", "Amount", "Series"]
    csvwriter.writerow(header)
    # @TODO: Write the values of each dictionary inside of `big_raisers`
    # as a row in the CSV file.
    # YOUR CODE HERE!

    for row in big_raisers:
        csvwriter.writerow(row.values())
