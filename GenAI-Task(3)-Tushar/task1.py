# Task 1 - Basic Function: Price After Discount



# Declare a function with two arguments 1 is for price and 1 is for discount percent with default value of discount = 5
def apply_discount(price , discount_percent = 5):


    # Extra optional to check that discount should not be greater than 60%
    if (discount_percent > 60):
        print(f"Discount value cannot be exceeds 60%")
    
    else:
        # Calculate discount
        discount_amount = price * (discount_percent / 100)
        price_after_discount = price - discount_amount

        # Display results
        print(f"Price: {price}")
        print(f"Discount: {discount_percent}%")
        print(f"Discount Amount: {discount_amount}")
        print(f"Price After Discount of {discount_percent}% : {price_after_discount}\n")

        # Return the final price
        return price_after_discount

# Take the 1 int type user input for price

price=int(input("Please enter price: "))


# 1. call apply discount function and pass price and 10% discount as a parameter in the function
apply_discount(price, 10)


# 2. call apply discount function and pass price and without passing discount so default 5% discount applicable
apply_discount(price)


# 3. call apply discount function and pass price and pass 70% discount to check the discount value never exceed 60%
apply_discount(price, 70)

