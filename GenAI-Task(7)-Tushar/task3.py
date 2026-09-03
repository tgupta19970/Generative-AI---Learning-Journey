# Task 3 - Inheritance Single Level

# Create a parent class
class Product:
    # Initialize the Constructor
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # create a get_info function to show basic product details
    def get_info(self):
        return f"Product Name: {self.name}, Price: {self.price}"

# Create a subclass
class ElectronicProduct(Product):

    # Taking parent attributes + warranty_years
    def __init__(self, name, price, warranty_years):
        super().__init__(name, price)
        self.warranty_years = warranty_years

    # Override get_info method
    def get_info(self):

        # Get basic name and price from the Parent class
        base_info = super().get_info()
        # return Product Name, price and warrenty Years
        return f"{base_info}, Warranty: {self.warranty_years} years"

# Create a object 
tv = ElectronicProduct("LED", 29999, 1)

# Call overridden get_info()
print(tv.get_info())


