## Task 2: Categories (Sets)

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

# Convert the list into a set
# A set removes duplicate categories
categories_set = set(categories)

# Print the unique categories
print("Categories set:", categories_set)

# Add a new category
categories_set.add("Wearables")

# Adding Electronics again does not create a duplicate
categories_set.add("Electronics")

# Print the updated set
print("Updated categories set:", categories_set)

# Check if Audio is present in the set
category_to_check = "Audio"

if category_to_check in categories_set:
    print(category_to_check + " exists in the set: True")
else:
    print(category_to_check + " exists in the set: False")

# Check if Furniture is present in the set
category_to_check = "Furniture"

if category_to_check in categories_set:
    print(category_to_check + " exists in the set: True")
else:
    print(category_to_check + " exists in the set: False")

# len() how many unique categories are in the set
print("Total unique categories:", len(categories_set))