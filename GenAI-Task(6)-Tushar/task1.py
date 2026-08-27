# Task 1 - Safe Division Utility

print("Please don't provide the value as 0")
# Take numerator and denominator from the user
numerator = input("Enter numerator: ")
denominator = input("Enter denominator: ")
try:
    # Convert the inputs into numbers
    numerator = float(numerator)
    denominator = float(denominator)

    # Divide the two numbers
    result = numerator / denominator
    
# Handle input that is not a number
except ValueError:
    print("Please enter valid numbers.")

 # Handle division by zero
except ZeroDivisionError:
    print("Cannot divide by zero.")

 # Return result becuase there is no error
else:
    print("Result:", result)

# This will always run
finally:
    print("Operation Complete")