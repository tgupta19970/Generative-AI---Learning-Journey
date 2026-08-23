# Task 7 - Mini Project : Export Discounted Prices

# Create the prices dictionary
prices = {
    "Mouse": 500,
    "Keyboard": 800,
    "Monitor": 7000,
    "Pendrive": 400,
    "Camera": 5000
}

# Ask user for discount percentage
discount_percent = int(input("Enter discount percentage: "))

# Calculate discounted prices and write into file
file = open("discount_report.txt", "w")
# Write header
file.write("Product | Original Price | Discounted Price\n")

total_discounted = 0
count = 0

for product, original_price in prices.items():
    discount_amount = original_price * (discount_percent / 100)
    discounted_price = original_price - discount_amount
    # Write each product line
    file.write(f"{product} | {original_price} | {discounted_price}\n")

    total_discounted += discount_amount
    count += 1


# Extra optional: Write summary at the bottom
average_discounted = total_discounted / count
file.write("\n")
file.write(f"Total Items: {count}\n")
file.write(f"Total total_discounted: {total_discounted}\n")

file.write(f"Average Discounted Price: {average_discounted}\n")
file.close()

print("\nDiscounted prices successfully written to discount_report.txt")

# Read the file and print it to the terminal
print("\nDiscount Report")
file = open("discount_report.txt", "r")
for line in file:
    print(line.strip())

file.close()