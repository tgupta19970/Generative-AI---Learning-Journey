# Task 4 - Using map(): Apply GST to List of Prices

# Create a Prices List:
pricesList=[100, 250, 400, 1200, 50]

# Print the Original Prices List
print(f"Orignal Price List: {pricesList}")

# Add 18% GST to each price 
priceWithGST = list(map(lambda price: price + (price * 0.18), pricesList))

# Print the prices after adding GST
print("Price List after adding GST:", priceWithGST)


