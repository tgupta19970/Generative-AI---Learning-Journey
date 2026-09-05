# Task 5 - Stastical Operations (Core Focus)

# Import numpy Library
import numpy as np 

# Given a Array 
marks = np.array([78, 85, 90, 66, 72, 88, 95, 60])

# Print Orignal Array
print(f"Orignal Marks Array: {marks}\n")



# Calculate Mean and show result
mean = np.mean(marks)
print(f"Mean: {mean}")

# Calculate Median and show result
median = np.median(marks)
print(f"Median: {median}")

# Calculate Variance and show result
variance = np.var(marks)
print(f"Variance {variance}")

# Calculate Standard Deviation and show result 
standard_deviation = np.std(marks)
print(f"Standard Deviation: {standard_deviation}")


# Calcualte Minimum and Maximum and show result
minimum = np.min(marks)
maximum = np.max(marks)

print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")

# Calculate range np.max() - np.min() and show result
range_value = np.max(marks) - np.min(marks)
print(f"Range: {range_value}") 
