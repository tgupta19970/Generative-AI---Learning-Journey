# Gen AI - Assignment 2 

This assignment helped me learn the basic Python how to handle if else condition and Discount calculation.

# Task 1: Discount Rule + Tax

This task is about using user input, if-else conditions, discount calculation, and tax calculation in Python.

What I Learned

In this task, I learned:

How to take integer type input from the user
How to use if, elif, and else
How to calculate a percentage
How to calculate discount
How to calculate tax
How to calculate the final amount
How It Works

Asks the user to enter an order amount.

Different discounts are applied based on the order amount

₹2000 or more - 15% discount
₹1500 to ₹1999 - 10% discount
₹1000 to ₹1499 - 7% discount
Below ₹1000 - No discount

After applying the discount, the program adds 5% tax and displays the final amount.


# Task 2: Process Multiple Orders (for loop)

This task is about using a for loop to process multiple orders.

What I Learned

In this task, I learned:

How to apply discount rules to multiple orders
How to calculate discount amounts on the multiple orders
How to calculate total revenue 
How to count orders that received a discount
How It Works

We have a list of different order amounts.

For each order, the program:

Checks the order amount.
Applies the discount based on the amount.
Calculates the discount.
Calculates the amount after discount.
Adds the amount to the total revenue.

At the end, the program displays the total revenue after discount.

Discount Rules
2000 or more - 15% discount
1500 to 1999 - 10% discount
1000 to 1499 - 7% discount
Below 1000 - No discount


# Task 3: User Menu (while loop + break/continue)

This Python program is a simple Order Management Menu that allows the user to:

- Add order amounts
- View all orders
- Calculate discounts
- Calculate the grand total
- Exit the program

The program uses a while loop to continuously display the menu until the user selects q.

Features

1. Add Order Amount
    - The user can enter an order amount.
    - The amount is stored in the orders list.
2. Show Orders and Totals
    - Displays all added orders.
    - Calculates the discount based on the order amount.
    - Displays the discounted amount.
    - Calculates the grand total.
3. Quit
    - Enter q or Q to exit the program.
4. Invalid Choice Handling
    - Displays an error message for an invalid menu choice.
    - Shows the menu again.


Discount Rules
2000 or more - 15% discount
1500 to 1999 - 10% discount
1000 to 1499 - 7% discount
Below 1000 - No discount

# Task 4: Loop Control With Conditions (break & continue)

This Python program processes a list of daily sales using a for loop.

It uses break and continue to handle different types of sales data.

How It Works
- If the sale is -1, it is treated as corrupted data and the loop stops using break.
- If the sale is 0, it means no sales for that day, so it is skipped using continue.
- For valid positive sales, the amount is added to total_sales.
- The running total is printed after each valid sale.
- The final total is printed after the loop.



# Run each task:
Open Terminal and go to main folder then run below command for run each task
```bash
python task1.py
python task2.py
python task3.py
python task4.py
```
Conclusion
This assignment helped me practice the below python topics:

1. while loop
2. for loop
3. if, elif, and else
4. break
5. continue
6. Lists
7. User input with input()
8. Type conversion using int()
9. String methods such as strip() and lower()
10. Basic arithmetic operations
11. Formatted strings using f-strings