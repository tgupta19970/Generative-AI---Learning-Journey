# Task 4 - Generate Summary Report from File

# Open file in the read mode
file = open("sales_data.txt", "r")
all_lines = file.readlines()

# Create a empty sales list to store each line into a integer
sales_list = []

for lines in all_lines:
    sales_list.append(int(lines.strip()))

print(f"After Reading and convert into integer list : {sales_list}")

# Calculate Total Sales 
total_sales = 0
for sales in sales_list:
    total_sales += sales

print(f"Total Sales : {total_sales}")

# Find Highest Sale by using max
highest_sale = max(sales_list)
print(f"Highest Sale : {highest_sale}")

# Find Lowest Sales by using sorted() function and indexing
sorted_sales_list = sorted(sales_list)
lowest_sales = sorted_sales_list[0]
print(f"Lowest Sale : {lowest_sales}")


# Calculate Average Sales
# find the length of total sales entry
length_total_sale = len(sales_list)

# Calculate average sales by dividing total sales by the total number of sales
average_sales = total_sales / length_total_sale
print(f"Average Sales : {average_sales}")


