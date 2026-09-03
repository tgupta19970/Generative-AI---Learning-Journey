# Task 6 - Magic Method & Operator Overloading

# Create a Product class
class Product:

    # Initialize the Constructor
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    # Magic method __str__() to return product details
    def __str__(self):
        return f"Product Details - (Name:{self.name}, Price: {self.price}, Category: {self.category})"

    # Magic method __add__() to overload the '+' operator for adding the price of two products
    def __add__(self, other):
        product_price = self.price + other.price
        return product_price

# Create two product objects
product1 = Product("Laptop", 1200, "Electronics")
product2 = Product("Mouse", 25, "Accessories")

# Result of checking for __str__() method with both prodcuts
print(product1)
print(product2)

# Print total price for combined price
total_price = product1 + product2
print(f"Total Combined Price: {total_price}")




