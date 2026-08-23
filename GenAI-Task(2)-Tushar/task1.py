# Assignment 2 - Task 1: Discount Rule + Tax

# Take a user input as an integer
order_amount = int(input("Enter the order amount: "))


# This condition check that input value should be integer only other wise throw error
if isinstance(order_amount, int):

    # Apply discount rule using if-else
    if order_amount >= 2000:
        discount_percent = 15  # 15% discount
    elif order_amount < 2000 and order_amount >= 1500:
        discount_percent = 10 # 10% discount
    elif order_amount < 1500 and order_amount >= 1000:
        discount_percent = 7 # 7% discount
    else:
        discount_percent = 0

    # Calculate discount
    discount_amount = order_amount * (discount_percent / 100)
    amount_after_discount = order_amount - discount_amount

    # Add 5% tax on the amount after discount
    tax_percent = 5
    tax_amount = amount_after_discount * (tax_percent / 100)
    final_total = amount_after_discount + tax_amount

    # Display results
    print(f"Order Amount: {order_amount}")
    print(f"Discount: {discount_percent}%")
    print(f"Discount Amount: {discount_amount}")
    print(f"Amount After Discount: {amount_after_discount}")
    print(f"Tax (5%): {tax_amount}")
    print(f"Final Total: {final_total}")

else :
    print(f"{order_amount} is a invalid value to execute this program")