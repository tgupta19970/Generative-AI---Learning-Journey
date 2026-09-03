# Task 7 - Mini Project: Simple Inventory System (OOP Only)


# create Product class to manage a single item in the store and also show to combine proce of two products
class Product:
    # Initialize the Constructor
    def __init__(self, name, price):
        self.name = name    
        self.price = price        

    # Operator overloading add two product price
    def __add__(self, other):
        return self.price + other.price

    
    # Magic method __str__() to return product details
    def __str__(self):
        return f"Product Details - (Name:{self.name}, Price: {self.price})"


# Create a Inventory Class
class Inventory:
    # Initialize the Constructor with empty list
    def __init__(self):
        self.products = []
    
    # Create a add product method
    def add_product(self, product):
        # Append product object to list
        self.products.append(product)
        print(f"Product added: (Name: {product.name}, Price: {product.price})")

    # Create a method to remove product by product name from list
    def remove_product(self, name):
        # Iterate the products list by for loop
        for product in self.products:
            # Convert the both product name in the lower case and check that its exist in the list or not
            if product.name.lower() == name.lower():
                # Remove matching product object from list
                self.products.remove(product)
                print(f"Removed '{name}' from inventory.")
                return
            else:
                print(f"Product '{name}' not found in inventory list.")

    # Create a method of get_total_value() to calculate the total price of all products
    def get_total_value(self):

        # Check is invetory list is empty or not
        if not self.products: 
            print("Inventory list is empty.")
            return

        # declare a variable to calculate total price
        total_price = 0
        # Iterate the products list by for loop
        for product in self.products:
            # Calcuate total price and store to the total_price 
            total_price = total_price + product.price
        return total_price

    # Creating a show_all_products() method to show all product info
    def show_all_products(self):
        # Check is invetory list is empty or not
        if not self.products: 
            print("Inventory list is empty.")
            return

        print("\nCurrent Inventory Products")
        count = 1
        # Iterate the products list by for loop
        for product in self.products:
            # Result of product info
            print(f"{count}. Product info: {product}")
            count += 1


# Create a Store class
class Store:
     # Initialize the attributes with empty list
    def __init__(self, store_name):
        self.store_name = store_name
        self.inventory = Inventory();

    # Create a method add_new_product and add 
    def add_new_product(self):
        # Takes user input and creates a new Product object
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        product = Product(name, price)
        self.inventory.add_product(product)
        print(f"Product '{name}' added successfully.")

    # Create show_summary Method to show the result of total number of items and total inventory value
    def show_summary(self):
        print(f"\nStore Name: {self.store_name}")
        total_items = len(self.inventory.products)
        total_value = self.inventory.get_total_value()
        print(f"Total items : {total_items}")
        print(f"Total value : {total_value}")
        self.inventory.show_all_products()

# Create a store object 
store_name = Store("Samsung")

# Adding 3 product by loop
print("Adding 3 products...")
i=0
while i < 3:
    store_name.add_new_product()
    i += 1

# 3. Showing summary of the store
store_name.show_summary()


# Using __add__() Method to combine price of two products

# first check that length should be >= 2
if len(store_name.inventory.products):

    p1 = store_name.inventory.products[0]
    p2 = store_name.inventory.products[1]

    combined_price = p1 + p2

    print(f"\nCombined price of '{p1.name}' and '{p2.name}': {combined_price}")
