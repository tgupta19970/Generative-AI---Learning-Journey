# Task 6 - Percentiles and Sorting

# Import numpy Library
import numpy as np 

# Using same Array 
marks = np.array([78, 85, 90, 66, 72, 88, 95, 60])

# Print Orignal Array
print(f"Orignal Marks Array: {marks}\n")

# Sort the array and show result
sorted_array = np.sort(marks)
print(f"Sorted Array: {sorted_array}")

# Find 25th Percentile, 50th Percentile and 75th Percentile and show result
percentile_25 = np.percentile(marks, 25)
percentile_50 = np.percentile(marks, 50)
percentile_75 = np.percentile(marks, 75)

print(f"25th Percentile: {percentile_25}")
print(f"50th Percentile: {percentile_50}")
print(f"75th Percentile: {percentile_75}")


