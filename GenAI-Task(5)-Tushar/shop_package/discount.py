# Task 3 - Create the simple package

# apply discount function
def apply_discount(price, percent):
    discount_price = price * (percent / 100)
    after_discount_final_price = price - discount_price
    return after_discount_final_price

# Flat Discount Function 50 & on the original price
def flat_discount(price):
    flat_discount = 50
    discount_price = price * (flat_discount / 100)
    after_flat_discount_final_price = price - discount_price
    return after_flat_discount_final_price
