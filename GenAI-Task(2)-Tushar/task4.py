# Assignment 2 - Task 4: Loop Control With Conditions (break & continue)

# list with the given value
daily = [200, 150, 0, 400, 50, -1, 300]

total_sales = 0

for sale in daily:
    # Stop if data is corrupted
    if sale == -1:
        print("The sales data is corrupted")
        break

    # Skip days with no sales
    if sale == 0:
        print("Sale data not found for oday")
        continue

    # Add valid sales
    total_sales += sale
    print("Running total:", total_sales)

print("Final total:", total_sales)


