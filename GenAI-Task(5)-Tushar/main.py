import math_utils
from math_utils import *
from math_utils import square
from string_utils import *
import shop_package.discount as disc
import shop_package.billing as bill
from shop_package.billing import *


# Task 1 - Create a simple module (math_utils.py)


# Use function with module name
cal_sum = math_utils.add(10, 20)
print("Sum of 2 numbers:", cal_sum)


# Calculate Substraction by import * 
cal_sub = subtract(20, 120)
print(f"Substraction: {cal_sub}\n")


# Calculate Square root by import * 
a = 16
sqrot = square(a)
print(f"Square root of {a}: {sqrot}\n")


# Calculate Square root by "import squareRoot" module
n = 10
sqrt = square(n)
print(f"Square root of {n}: {sqrt}\n")



# Task 2 - Create a Another Module (string_utils.py)

# Return Text Each word is capitalized
word = "Hello World"
capitalizedWord = capitalize_words(word)
print(f"After Capitalized Words: {capitalizedWord}\n")


# Convert to string to Reverse String
text = "Python"
revString = reverse_string(text)
print(f"After Reversed the String: {revString}\n")


# Return Total Number of Word in Text
wordString = "Python is a very easy language"
total_words = word_count(wordString)
print(f"Total number of words in the string of '{wordString}': {total_words}\n")


# Task 4 - Importing the packages in main.py

# Result of apply discount
price = 11000
percent = 10
applyDiscount = disc.apply_discount(price, percent)
print(f"After applied the {percent}% of price {price}, Final Price: {applyDiscount}\n")


# Result of flat 50% discount
flatPrice = 11000
flatDiscount = disc.flat_discount(flatPrice)
print(f"After applied the flat 50% discount, The Final Price: {flatDiscount}\n")


# Result Calculate total
sumlist=[100, 200, 300]
total_value = bill.calculate_total(sumlist)
print(f"Calculate Total Value : {total_value}")


# Result Add 5 % tax
basic_price=2000
price_with_tax = apply_tax(basic_price)
print(f"Price With 5% Tax : {price_with_tax}")
