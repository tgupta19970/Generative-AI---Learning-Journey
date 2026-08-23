# Task 5 - Using filtter(): Filter Expensive Product

# Create a price list
prices = [100, 250, 400, 1200, 50, 2000, 850]

# By using filter() and lambda function, filter the list of prices which price value is greater than 500
greater_price_list = list(filter(lambda x:x>500, prices))

# Print the list of price which values are greater than 500
print(f"Price greater than 500: {greater_price_list}")

# By using filter() and lambda function, filter the list of prices which price value is less than or equals to 500
less_or_equal_price_list = list(filter(lambda x:x <= 500, prices))

# Print the list of price which values are less than or equals to 500
print(f"Price less than or equals to 500: {less_or_equal_price_list}")
