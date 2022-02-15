"""The 401k Shuffle."""

# 1. @TODO: Use the following dictionary or paste the dictionary to a new python script:
accounts = {"Schwab": 2000, "Fidelity": 8000, "Merrill": 3000, "Wells Fargo": 0.01}

# 2. @TODO: Using dictionary syntax, print the amount of the Fidelity 401k.
# YOUR CODE HERE!

print(accounts["Fidelity"])

# 3. @TODO: What’s up with that one penny Wells Fargo account?
# Delete that account from the dictionary.
# YOUR CODE HERE!
del accounts["Wells Fargo"]

# Add the new 401k account (this one’s with SoFi)
# to the list of existing accounts.
# YOUR CODE HERE!
accounts["Sofi"] = 2000

# 5. @TODO: Create a new dictionary to store the new 401k rollover
# First copy the following list:
# YOUR CODE HERE!

rollover = list(accounts.values())

# 6. @TODO: Sum up your money from the `old_account_amounts` list
# Save this total amount to a new variable called `total_amount`.
# YOUR CODE HERE!
total_amount = sum(rollover)

# 7. @TODO: Finally, create a new dictionary called `new_accounts`.
# YOUR CODE HERE!
new_accounts = {}

# Store the new 401k as a new entry.
# YOUR CODE HERE!
new_accounts["WealthFront"] = total_amount

# Print the new_accounts dictionary
print(new_accounts)