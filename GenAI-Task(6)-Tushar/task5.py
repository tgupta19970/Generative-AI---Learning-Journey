# Task 5 - Mini Program: Safe Shopping Cart

# Create a safe shopping cart function
def shopping():

    # Create a empty cart list
    cart = []

    total_item = 0

    while True:

        # Ask user to enter price
        price = input("Please enter price:")

        # Check if user enter the q/Q
        if price.lower() == "q":
            break

        # try Block start
        try:

            # Convert input price to float
            converted_price = float(price)
            
            # check price value negative condition
            if (converted_price < 0):
                raise Exception("Negative price not allowed")

            # Add valid price to the cart list
            cart.append(converted_price)

       
        

       
        # Handle non numeric string   
        except ValueError:
            print("Invalid input, please enter a valid number")


        # Handle negative price exception
        except Exception as error:
            print(error)


    # Result show
    print(f"Total items: {len(cart)}")
    print(f"Total bill: {sum(cart)}")
        

shopping()