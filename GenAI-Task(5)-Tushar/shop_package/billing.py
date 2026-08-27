# Task 3 - Create the simple package


# Calculate Sum of all price
def calculate_total(prices):
    total_amount = 0
    for price in prices:
        total_amount = total_amount + price

    return total_amount

# Add 5% Tax Function 
def apply_tax(price):
    calculate_tax = price * (5 / 100)
    after_add_tax = price + calculate_tax

    print(f"Actual Price; {price}")
    print(f"5 % tax amount price of: {calculate_tax}")
    return after_add_tax
