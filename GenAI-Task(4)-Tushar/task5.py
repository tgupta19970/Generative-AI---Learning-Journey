# Task 5 - Create Product Into File (User Input) 

print("Enter details of 3 products:\n")


# create a dict for storing the product details 
product_dic = {}

# Iterate the loop 3 times
for i in range(3):
    # Ask the user for 3 product names and thier prices
    name = input(f"Enter Product Name {i+1}: ")
    price = int(input(f"Enter Product Price {i+1}: "))
    product_dic[name] = price

print(f"After adding all three products {product_dic}")

# Write the dictionary into products.txt in the format "ProductName | Price"
file = open("products.txt", "w")

# Used this count function to manage empty line
count = 0

# Iterate the product_dic by using loop
for name, price in product_dic.items():

    if count > 0:
        file.write(f"\n{name} | {price}")

    else:
        file.write(f"{name} | {price}")

    count += 1

file.close()
    

# Step 4: Read the file and print each line with proper formatting
print("\nProducts from File")

file = open("products.txt", "r")
product_count = 1
for product_line in file:
    print(f"Product {product_count} = {product_line.strip()}")
    product_count += 1

file.close()