# Task 3: Product Pricing (Dictionaries)

# Create a dictionary with product prices
price_dict = {
    "Laptop": 899.99,
    "Smartphone": 699.50,
    "Headphones": 149.99,
    "Keyboard": 79.99,
    "Monitor": 249.00,
    "Mouse": 39.99
}

# Print the original dictionary
print("Original price_dict:", price_dict)

# Add a new product
price_dict["Webcam"] = 59.99
print("After adding Webcam:", price_dict)

# Update the price of Laptop
price_dict["Laptop"] = 849.99
print("After updating Laptop price:", price_dict)

# Try to remove a product
product_to_remove = "Tablet"

# Check first because Tablet may not exist
if product_to_remove in price_dict:
    del price_dict[product_to_remove]
    print(product_to_remove + " removed successfully.")
else:
    print(product_to_remove + " does not exist in the dictionary.")

# Remove Mouse if it exists
if "Mouse" in price_dict:
    del price_dict["Mouse"]
    print("Mouse removed successfully.")

# Print the dictionary after removing products
print("After removals:", price_dict)

# Add all prices together
total_price = sum(price_dict.values())

# Divide the total by the number of products
average_price = total_price / len(price_dict)

# Round the answer to 2 decimal places
print("Average price of all products:", round(average_price, 2))


# Start with the first product as the highest price
max_product = None
max_price = 0

# Start with a very high value for the lowest price
min_product = None
min_price = 999999

# Check each product one by one
for product, price in price_dict.items():

    # Check if this price is higher than the current highest price
    if price > max_price:
        max_price = price
        max_product = product

    # Check if this price is lower than the current lowest price
    if price < min_price:
        min_price = price
        min_product = product

# Print the product with the highest price
print("Product with maximum price:", max_product)
print("Maximum price:", max_price)

# Print the product with the lowest price
print("Product with minimum price:", min_product)
print("Minimum price:", min_price)