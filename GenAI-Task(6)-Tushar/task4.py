# Task 4 - File Reader with Exception Handling

# Ask the user to enter a filename
filename = input("Enter the filename: ")

# Start a try block to handle error
try:
    line_count = 1
    # Open the file in read mode
    file = open(filename, "r")
    
    # Read all lines
    lines = file.readlines()
    
    # Iterate first 3 lines 
    for line in lines[:3]:
        print(f"Line number {line_count}. ", line.strip())

        line_count+=1
        
    # Close file
    file.close()

# FileNotFoundError if file does not exist
except FileNotFoundError:
    print("File not found.")

# PermissionError if permission not allowed
except PermissionError:
    print("Permission denied.")

# finally block
finally:
    print("File operation attempted.")