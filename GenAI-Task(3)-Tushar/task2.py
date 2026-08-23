# Task 2 - Recursive Function - Factorial Utility

# declare a factorial function with n argument
def factorial(n):

    # check condition that value should not be negative 
    if n < 0:
        return f"Negative value is not allowed"
    
    # Handle two edge cases: n == 0 or n == 1
    elif n == 0 or n == 1:
        return n
    
    # Calculate Factorial
    else:
        return n * factorial(n - 1)


# Take int type user input
factorial_input = int(input("Please enter value: "))

# Call the factorial function with user input
print(f"The Factorial of {factorial_input} = {factorial(factorial_input)}")