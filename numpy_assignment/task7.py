# Task 7 - Mini Use Case: Sales Analysis

# Import numpy Library
import numpy as np 

# Given daily sales data
sales = np.array([1200, 1500, 900, 2000, 1800, 1700, 1600])

# Print Orignal Array
print(f"Orignal Sales Array: {sales}\n")

# Calcualte total Weekly Sales 
total_weekly_sales = np.sum(sales)
print(f"Total Weekly Sales: {total_weekly_sales}")

# Calculate Average Daily Sales
average_daily_sales = np.mean(sales)
print(f"Average Daily Sales : {average_daily_sales:.2f}")

# Calculate Highest and Lowest Sales day
highest_sales = np.max(sales)
lowest_sales = np.min(sales)
print(f"Highest Sales Day: {highest_sales}")
print(f"Lowest Sales Day: {lowest_sales}")

# Calculate Standard Deviation 
standard_deviation = np.std(sales)
print(f"Standard Deviation: {standard_deviation:.2f}")


