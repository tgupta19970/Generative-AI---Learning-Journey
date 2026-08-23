# Task 3 - Append New Sales Entry into the sale File

# Open file in the wirte mode
file = open("sales_data.txt", "a")

# Create a list with the Given new Sales record
sales_list = [5000, 2500, 1700]

# iterate the list by using for loop and write each entry in sales_data.txt file line by line
for price in sales_list:

    # for writing the content line by line
    file.write("\n"+str(price))\

# Close the file
file.close()

# Reopen the file again for print the content
readFile = open("sales_data.txt", "r")
content = readFile.read()
print("After Appending Print the Entire Updated File")
print(content)
readFile.close()