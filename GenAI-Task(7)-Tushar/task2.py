# Task 2 - Constructor & Encapsulation

# Create a prodct class
class Product:

    # Initialize the Constructor with price a private attribute
    def __init__(self, name, price):
        self.name = name
        # Make a price is a private attribute
        self.__price = price


    # Create a gettter method get_price()
    def get_price(self):
        return self.__price

    # Create a setter method set_price()
    def set_price(self, price):
        # Update price value only if price > 0:
        if price > 0:
            self.__price = price
        else :
            print("\nProduct value should be greater than 0")

# Create a product 
product1 = Product("Audio", 1000)

# Result of get_price method with product 1
print(f"Price : {product1.get_price()}")

# set new price with set_price() method 
update_price = product1.set_price(0)
print(f"\nAfter update the new Price : {product1.get_price()}")

