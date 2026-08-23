# Task 6 - Combined Utility Function

# Create a general fucntion
def process_prices(prices):

    # By Using map() + lambda functions, calculate the discount of 10%
    discount_list = list(map(lambda price : price - (price * 10 / 100), prices))

    # By Using filter() + lambda functions, for finding the price value that is above 300 after discount
    filter_price_list = list(filter(lambda price : price > 300,  discount_list))

    # Return Both list
    return discount_list, filter_price_list

# Create a list of prices
prices = [100, 500, 900, 50, 750]

#  call process_prices function and pass the list
discounted_prices, filtered_prices = process_prices(prices)

# Print the results
print("Discounted prices:", discounted_prices)
print("Filtered prices:", filtered_prices)