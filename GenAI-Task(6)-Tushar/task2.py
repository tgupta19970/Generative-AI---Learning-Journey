# Task 2 - Bill Calculator with Error Handling


# Create a bill calculator function
def bill_calculator(priceList):

    total_price = 0
    # Iterate the prices list by using for loop
    for price in priceList:

        try: 
            # Check it is a number (int or float)
            if not isinstance(price, (int, float)):
                raise TypeError("value is not a number")

            # Check for negative price
            
            if price < 0:
                raise ValueError("Negative price not allowed")

            # Calculate total price
            total_price = total_price + price

            print(f"Running total: {total_price}")

        except TypeError as error:
            print(f"'{price}' is not a number")
            continue
        
        except ValueError as valueError:
            print(f"'{price}' Negative price can not be allowed")
            continue

    return total_price


# Given a list of product prices
prices = [120, 350, 'abc', 500, -200, 800]

# Call billCalculator function
total_bill = billCalculator(prices)

print(f"Final Total: {total_bill}")