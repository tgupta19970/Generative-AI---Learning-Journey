# Task 3 - Important Numpy Mathematical Formulas

# Import numpy Library
import numpy as np 

# Given Array
value = np.array([2, 4, 6, 8, 10])

# Calculate square root of each element and show result
sqrt_array = np.sqrt(value)
print(f"Orignal Array : {value}\n\n")
print(f"Square root of each element: {sqrt_array}")

# Calculate Exponential of each element and show result
exp_array = np.exp(value)
print(f"Exponential of each element: {exp_array}")


# Calculate Natural Logarithm of each element and show result
nl_array = np.log(value)
print(f"Natural Logarithm of each element: {nl_array}")

# Calculate Sum of the all elements and show result
sum_arrar = np.sum(value)
print(f"Sum of the all elements: {sum_arrar}")


# Calculate Cumulative Sum and show result
cumsum_arrar = np.cumsum(value)
print(f"Cumulative Sum: {cumsum_arrar}")

