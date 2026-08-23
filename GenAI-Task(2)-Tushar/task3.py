# Assignment 2 - Task 3: User Menu (while loop + break/continue)

# list to store order amounts
orders = []   

# while true because whille loop will run until user not quit
while True: 

    # Display the menu options
    print("\nORDER MENU")
    print("1 Add order amount")
    print("2 Show all orders and totals")
    print("q Quit \n")

    # Take user choice and convert to lowercase for easy comparison
    choice = input("Enter your choice: ").strip().lower()

    # Option 1: Add a new order amount
    if choice == "1":
        # Take order amount input as integer
        amount = int(input("Enter order amount: "))
        # Add the amount in the orders list
        orders.append(amount)
        print(f"Order of {amount} added successfully.")
        continue
    
    # Option 2: Show all orders with discount
    if choice == "2":
        # Check if any orders exist
        if len(orders) == 0:
            print("No orders added yet.")
            continue

        print("\n Order Summary")
        grand_total = 0   # To store sum of all final amounts

        # Loop through each order in the list
        for i in range(len(orders)):
            order_amount = orders[i]
            # Now apply discount rule using if-else
            if order_amount >= 2000:
                discount_percent = 15  # 15% discount
            elif order_amount < 2000 and i >= 1500:
                discount_percent = 10 # 10% discount
            elif order_amount < 1500 and i >= 1000:
                discount_percent = 7 # 7% discount
            else:
                discount_percent = 0


            # Calculate discount amount and amount after discount
            discount_amount = order_amount * (discount_percent / 100)
            amount_after_discount = order_amount - discount_amount

            grand_total += amount_after_discount

            # Display details of current order

             # Display results
            print(f"Order Amount {i+1}: {order_amount}")
            print(f"Discount: {discount_percent}%")
            print(f"Discount Amount: {discount_amount}")
            print(f"Amount After Discount: {amount_after_discount}")

        # Display the grand total of all orders
        print(f"\nGrand Total of all orders: {grand_total}")

         # Show the menu again
        continue

    # Option q/Q: Exit the program
    elif choice == "q":
        print("Exiting the program. Thank you!")
        break   # Exit the while loop

    # Handle any invalid menu choice
    else:
        print("Invalid choice! Please try again.")
        continue   # Go back to the top of the loop and show menu again


