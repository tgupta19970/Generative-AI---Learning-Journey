# Task 2 - Important Mathmatical Operations

# Import numpy Library
import numpy as np 

# Given two array A and B
A = np.array([10, 20, 30, 40])
B = np.array([1,2,3,4])

# Orignal Array A and B
print(f"Orignal Array A: {A}")
print(f"Orignal Array B: {B}")

# Addition of both Array and show result
add_array_value = np.add(A, B)
print(f"The Result of Addition (A + B): {add_array_value}")

# Sbtraction of Array (A - B) and show result
subtraction_array_value = np.subtract(A, B)
print(f"The Result of Subtraction (A - B): {subtraction_array_value}")

# Multiplication of Array (A * B) and show result
multiple_array_value = np.multiply(A, B)
print(f"The Result of Multiplication (A * B): {multiple_array_value}")

# Divided of Array (A / B) and show result
divided_array_value = np.divide(A, B)
print(f"The Result of Divided (A / B): {divided_array_value}")

# Power (A ** 2) and show result
sqrt_array = np.power(A, 2)
print(f"The Result of Square Root of (A ** 2): {sqrt_array}")