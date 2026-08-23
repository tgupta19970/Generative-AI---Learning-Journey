# Task 1: Product Collections (Lists & Tuples)

# Create a list of products
products = [
    "Laptop",
    "Smartphone",
    "Headphones",
    "Keyboard",
    "Monitor",
    "Mouse"
]

# Create a tuple because the product has fixed details
sample_product = ("Laptop", 899.99, "Electronics")

# Index 1 means the second item in the list
print("2nd product:", products[1])

# -1 means the last item in the list
print("Last product:", products[-1])

# Add two new products to the list
products.append("Webcam")
products.append("USB Hub")

# Print the list after adding new products
print("Updated products list:", products)

# Convert the tuple into a list because tuples cannot be changed
sample_list = list(sample_product)

# Change the price in the list
sample_list[1] = 799.99

# Convert the list back into a tuple
sample_product = tuple(sample_list)

# Print the updated tuple
print("Updated sample_product:", sample_product)