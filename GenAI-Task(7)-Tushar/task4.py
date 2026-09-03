# Task 4 - Polymorphism

# Create a parent class
class Product:
    # Initialize the Constructor
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # create a get_info function to show basic product details
    def get_info(self):
        return f"Product Name: {self.name}, Price: {self.price}"



# Create a Laptop subclass
class Laptop(Product):

    # Taking parent attributes + warranty_years
    def __init__(self, name, price, warranty_years):
        super().__init__(name, price)
        self.warranty_years = warranty_years

    # Override get_info method
    def get_info(self):

        # Get basic name and price from the Parent class
        base_info = super().get_info()
        # return Product Name, price and warrenty Years
        return f"Laptop - {base_info}, Warranty: {self.warranty_years} years"



# Create a Mobile subclass
class Mobile(Product):

    # Taking parent attributes + warranty_years
    def __init__(self, name, price, warranty_years):
        super().__init__(name, price)
        self.warranty_years = warranty_years

    # Override get_info method
    def get_info(self):

        # Get basic name and price from the Parent class
        base_info = super().get_info()
        # return Product Name, price and warrenty Years
        return f"Mobile - {base_info}, Warranty: {self.warranty_years} years"


# Create Objects of Laptop and Mobile
laptop = Laptop("Mac Book", 100000, 3)
mobile = Mobile("iPhone 17", 80000, 2)

# put both objects into a list
products = [laptop, mobile]


# Iterate the product list to show Pholymorphism for each item
for product in products:
    print(product.get_info())