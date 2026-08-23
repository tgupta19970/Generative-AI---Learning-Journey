# Task 3 - Lambda Function: GST Calculator

# Take the int type user input for price
price_input = int(input("Please enter price: "))

# Create Lambda Function
gst = lambda price : price + (0.18 * price)

# Show Result
print(f"After added the 18% GST, the total price is {gst(price_input)}")

# Extra (optional): Lambda to compute final price after GST + Discount
final_price_after_gst_discount = lambda price, discount_per: (price - (price * discount_per / 100) * 0.18)

# Test the extra lambda with 18% GST + 10% discount 
print(f"\nFinal price after 10 percent discount + 18 percent GST on {price_input}:", final_price_after_gst_discount(price_input, 10))

# Test the extra lambda with 18% GST + 5% discount 
print(f"Final price after 5 discount + 18 percent GST on {price_input}:", final_price_after_gst_discount(price_input, 5))


