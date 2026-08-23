# Task 6 - Read File Safely (Error Handling inside file handling only)
# Import OS
import os
# Ask the user to file name to open
file_name = input("Please enter file name to open :")


# Check file exist or not by using if-else statement
if os.path.exists(file_name):
    print("File exists")

    # open the file again for print the content
    file = open(file_name, "r")
    content = file.read()
    print(content)
    file.close()

else:
    print("File not found, please check the file name")