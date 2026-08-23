# Task 1 - Write Sales Record To File

# Create a list of sales amount
sales = [1200, 450, 980, 1500, 3000]

# Used this count function to check empty line
count = 0

# Create file in the wirte mode
file = open("sales_data.txt", "w")


# iterate the list by using for loop and write each entry in sales_data.txt file line by line and comma-seperated format
for price in sales:

    if (count > 0):
        # for writing the content line by line
        file.write("\n"+str(price))

    else :
        file.write(str(price))

    count += 1

    # # Extra Optional - Write the data in comma-seperated format
    # file.write(str(price)+", ")

# # Close the file
file.close()

# Reopen the file again for print the content
readFile = open("sales_data.txt", "r")
content = readFile.read()
print(content)
readFile.close()






