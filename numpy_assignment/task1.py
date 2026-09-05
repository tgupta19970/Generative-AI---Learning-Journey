# Task 1 - Creating Numpy Arrays

# Import numpy Library
import numpy as np 

# Create a 1D array on integers 1 to 10
OneD_Array = np.arange(1, 11) 

# Create a 2D array of shape (3, 3) with value from 1 to 9 
TwoD_Array = np.arange(1, 10).reshape(3, 3)

# Numpy Array with the Given list
Numpy_Array = np.array([10, 20, 30, 40, 50])


# Result the shape of Each Array
print("1D Array:")
print(OneD_Array)
print("\n2D Array:")
print(TwoD_Array)
print("\nNumpy Array from List:")
print(Numpy_Array)

# Result the shape and data type of each array
print("\nShape and Data Type:")

print(f"1D Array Shape: {OneD_Array.shape}")
print(f"1D Array Data Type: {OneD_Array.dtype}")

print(f"2D Array Shape: {TwoD_Array.shape}")
print(f"2D Array Data Type: {TwoD_Array.dtype}")

print(f"Numpy Array Shape: {Numpy_Array.shape}")
print(f"Numpy Array Data Type: {Numpy_Array.dtype}")