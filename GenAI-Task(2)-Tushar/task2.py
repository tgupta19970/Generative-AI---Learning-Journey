# Assignment 2 - Task 2: process multiple orders (for loop)

# list with the given value
orders = [1200, 2500, 800, 1750, 3000]

# for calculating number of order discount received
discount = 0

# for calculating total revenue after discount
total_revenue = 0


# execute the loop for iterate the orders list
for i in orders:

    # Now apply discount rule using if-else
    if i >= 2000:
        discount_percent = 15  # 15% discount
        discount = discount + 1
    elif i < 2000 and i >= 1500:
        discount_percent = 10 # 10% discount
        discount = discount + 1
    elif i < 1500 and i >= 1000:
        discount_percent = 7 # 7% discount
        discount = discount + 1
    else:
        discount_percent = 0

     # Calculate discount
    discount_amount = i * (discount_percent / 100)
    amount_after_discount = i - discount_amount

    # Calculate Total Revenue
    total_revenue = total_revenue + amount_after_discount

    # Display results
    print(f"Order Amount: {i}")
    print(f"Discount: {discount_percent}%")
    print(f"Discount Amount: {discount_amount}")
    print(f"Amount After Discount:{amount_after_discount}\n")

# Total revenue after discount
print(f"Total revenue after discount : {total_revenue}\n")



# Extra (Optional) number of orders that received a discount
if discount_percent > 0 :
    print(f"Total number of discount received : {discount}\n")
