
# Gen AI - Assignment 3 Functions: (User-Defines, Recursive, Lambda, Map, Filter)

# ######################################################
# Task 1 - Basic Function: Price After Discount
# Apply Discount Function

This task is about learning how to create and use a function with arguments and a default value in Python.

What I Learned

In this task, I learned:

- How to create a function
- How to pass arguments
- How to use a default argument
- How to return a value from a function
- How to use if-else inside a function
- How It Works

The function is called:

apply_discount(price, discount_percent=5)

The function takes:

price - The product price
discount_percent - Discount percentage, with a default value of 5%

The program checks that the discount does not go above 60%.

Function Calls

The function is called three times:

apply_discount(price, 10)

This applies a 10% discount.

apply_discount(price)

This uses the default 5% discount.

apply_discount(price, 70)

This checks the rule that the discount cannot be more than 60%.


# ######################################################
# Task 2 - Recursive Function: Factorial Utility
# Factorial Function

This task is about creating a factorial function using recursion in Python.

What I Learned

In this task, I learned:

- How to create a function
- How to pass an argument to a function
- How recursion works
- How to handle negative numbers
- How to handle 0 and 1
- How It Works

The factorial() function calls itself with n - 1 until it reaches 0 or 1.

For example:

5! = 5 × 4 × 3 × 2 × 1 = 120

Negative numbers are not allowed.


# ######################################################
# Task 3 - Lambda Function: GST Calculator
# GST Calculation Using Lambda

This task is about learning how to use a Lambda function in Python.

What I Learned

In this task, I learned:

How to create a Lambda function
How to pass values to a Lambda function
How to calculate 18% GST
How to calculate discount and GST together
How It Works

The first Lambda function adds 18% GST to the given price.

gst = lambda price: price + (0.18 * price)

The second Lambda function is used to calculate the price after applying a discount and GST.


# ######################################################
# Task 4: Using map() - Apply GST

This task is about using map() and lambda functions in Python.

What I Learned

- How to use map()
- How to use a lambda function
- How to add 18% GST to each price in a list by using map()
# ######################################################


# Task 5: Using filter() - Filter Expensive Products

This task is about using filter() and lambda in Python.

What I Learned
- How to use filter()
- How to use a lambda function with filter()
- How to filter values based on a condition


I learned that filter() can be used to select values from a list based on a condition.

In this task, I used it to separate prices that are greater than 500 and prices that are less than or equal to 500.
# ######################################################
# ask 6: Combined Utility Function

This task is about using functions, map(), filter(), and lambda together.

What I Learned
- How to create a function
- How to use map() to apply a discount
- How to use filter() to select prices
- How to return two lists from a function
- How It Works

The function process_prices():

* Takes a list of prices.
* Applies a 10% discount using map().
* Keeps prices above 300 using filter().
* Returns both lists.


My Learning

This task helped me understand how map() and filter() can be used together inside a function.

I also learned how a function can return more than one value.
# ######################################################
# Task 7 - Mini Problem: Menu using Functions
Description

A simple Python program that uses functions to manage a list of prices.

Features
1. Add a price
2. Calculate average price
3. Find maximum price
4. Quit the program

Concepts Used
- Functions
- Lists
- if-else
- for loop
- while loop
- break and continue
- User input


# ######################################################
# Run each task:
Open Terminal and go to main folder then run below command for run each task
```bash
python task1.py
python task2.py
python task3.py
python task4.py
python task5.py
python task6.py
python task7.py


```
Conclusion
This assignment helped me practice the below python topics:

1. User-Defined Function
2. Recursive Function
3. Lambda Function
4. Map()
5. Filter()
6. Defualt Argument()