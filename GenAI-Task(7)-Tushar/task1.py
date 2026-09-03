# Task 1 - Basic Class & Object Creation

# Create a Product class
class Product:

    # Initialize the Constructor
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    # Create get_info Method for the result
    def get_info(self):
        print(f"Product Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Product Category: {self.category}")


    # Create a apply_dicount(percent) method
    def apply_dicount(self, percent):
        discount = self.price * percent / 100
        return self.price - discount



#  Create a first product object
product1 =  Product("Laptop", 60000, "Electronic")

# Create a second product object
product2 = Product("Head Phone", 5000, "Audio")

# Call get_info() for the first product
print("Product 1: ")
product1.get_info()

# Call get_info() for the second product
print("\nProduct 2: ")
product2.get_info()

# Call Extara optional apply_discount() 10% on the product1
after_discount = product1.apply_dicount(10)
print(f"\nAfter applied 10% discount on Product 1: {after_discount}")
