# Task 3 - Custom Exception: Age Validator 

# Create a check_age function
def check_age(age):
    try:

        # Check age: it is not exist between 1 to 120 
        if age < 1 or age > 120:
            raise ValueError("Age must be between 1 and 120")
        
        else :
            return "Your age has been validated successfully"


    except ValueError as valueError:
        return "Invalid Age, it must be between 1 and 120"



# Take Age Integer User Input
age = int(input("Please enter your age: "))
# Call check_age function
age_cal = check_age(age)
print(age_cal)