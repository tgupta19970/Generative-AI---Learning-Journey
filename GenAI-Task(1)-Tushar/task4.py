# Task 4: Combined Operations

# Create a list of products
products = [
    "Laptop",
    "Smartphone",
    "Headphones",
    "Keyboard",
    "Monitor",
    "Mouse",
    "Webcam",
    "USB Hub"
]

# Create a category for each product
categories = [
    "Electronics",
    "Electronics",
    "Audio",
    "Accessories",
    "Electronics",
    "Accessories",
    "Electronics",
    "Accessories"
]

# Store the price of each product in a dictionary
price_dict = {
    "Laptop": 849.99,
    "Smartphone": 699.50,
    "Headphones": 149.99,
    "Keyboard": 79.99,
    "Monitor": 249.00,
    "Mouse": 39.99,
    "Webcam": 59.99,
    "USB Hub": 24.99
}

# Create an empty list to store all product details
catalog = []

# Use the same position from products and categories
for i in range(len(products)):

    # Get the product name
    product_name = products[i]

    # Use the product name to get its price
    price = price_dict[product_name]

    # Get the category from the same position
    category = categories[i]

    # Store all three values together as a tuple
    catalog.append((product_name, price, category))


# Print all the products in the catalog
print("Catalog:")

for item in catalog:
    print(item)


# Create an empty dictionary
# This will store each category and its products
category_to_products = {}

# Go through each product in the catalog
for product_name, price, category in catalog:

    # If the category is not in the dictionary,
    # create an empty list for that category
    if category not in category_to_products:
        category_to_products[category] = []

    # Add the product to its category
    category_to_products[category].append(product_name)


# Print all products according to their category
print("\nCategory to Products:")

for category, product_list in category_to_products.items():
    print(category + ":", product_list)


# Start with zero as the highest product count
max_count = 0

# This will store the category with the most products
max_category = None

# Check each category
for category, product_list in category_to_products.items():

    # Count the products in the current category
    count = len(product_list)

    # If this category has more products,
    # save its name and count
    if count > max_count:
        max_count = count
        max_category = category


# Print the category with the most products
print("\nCategory with maximum products:", max_category)
print("Number of products:", max_count)

# Print all products in that category
print("Products in category:", category_to_products[max_category])