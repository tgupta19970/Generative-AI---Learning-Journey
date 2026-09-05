# Task 4 - Aggregation Operations

# Import numpy Library
import numpy as np 

# Given a 2D Array 
data = np.array([
    [10, 20, 30], 
    [40, 50, 60], 
    [70, 80, 90]
])

# show orignal array
print("Orignation 2D Array:")
print(data, "\n")

# Find Row wise Sum by using axis=1 and show result
row_wise_sum = np.sum(data, axis=1)
print(f"Row wise Sum: {row_wise_sum}")


# Find Column wise Sum by using axis=0 and show result
col_wise_sum = np.sum(data, axis=0)
print(f"Column wise Sum: {col_wise_sum}")


# Find Minimum and Maximaum Value from 2D Array and show result
# Minimum Value 
min_value = np.min(data)
print(f"Minimum Value in 2D Array: {min_value}")

# Maximum Value 
max_value = np.max(data)
print(f"Maximum Value in 2D Array: {max_value}")

# Find overall Mean of 2D Array
overall_mean = np.mean(data)
print(f"Overall Mean of 2d Array: {overall_mean}")