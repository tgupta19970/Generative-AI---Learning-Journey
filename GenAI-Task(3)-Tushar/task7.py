# Task 7 - Mini Problem: Menu using Functions

#  Create a function add_price() 
def add_price(price_list, price):

    # Handle the list length if it is 0, by using if else statement 
    if len(price_list) == 0:
        return "Price list is empty"
    else :
        # Adds the price in to price_list by using append function
        price_list.append(price)
        # return price_list
        return price_list


#  Create a function get_average_price() to get the average
def get_average_price(price_list):

     # Handle the list length if it is 0, by using if else statement 
    if len(price_list) == 0:
        return "Price list is empty"
    else :
        # create two variables to store the total price and the total count
        total = 0
        count = 0

        # Iterate the price list by using for loop
        for price in price_list:

            # Add the current price to the total
            total = total + price

            # Increase the count by 1
            count += 1

        # Calculate average price of the list
        average = total / count

        # return average
        return average



#  Create a function get_max_price() to get the max price value
def get_max_price(price_list):
     # Handle the list length if it is 0, by using if else statement 
    if len(price_list) == 0:
        return "Price list is empty"
    else :
        # get the maximum price by using max function
        return max(price_list)




# Create a menu function for manage the all above functions
def menu():
    # Create a empty price_list to store all the prices entered by the user
    price_list = []

    # run A while loop true till user will not quit
    while True:
        print("\n ---Menu--- \n")
        print("1 Add Price")
        print("2 Show Average Price")
        print("3 Show Maximum Price")
        print("4 Quit\n")

        # Ask user for thier choice
        user_input = input("Enter your choice : ")

        # Option 1 - ask user for a price and add it to the price list
        if user_input == "1":
            # Ask user for a price
            price = int(input("Please enter price: "))
            # add price to the price list by using append fucntion
            price_list.append(price)
            # show price list
            print(f"Price {price} added. Current list : {price_list}")
            # use continue function to continue the loop again
            continue
        
        # Option 2 - Calculate and display the average price
        elif user_input == "2":
            # call get_average_price function and store the value to the average value
            average = get_average_price(price_list)
            print(f"Average Price: {average}")
            # use continue function to continue the loop again
            continue

        # Option 3 - Calculate and display the maximum price
        elif user_input == "3":
            # call get_max_price function and store the value to the maximum value
            maximum = get_max_price(price_list)
            print(f"Maximum Price: {maximum}")
            # use continue function to continue the loop again
            continue

        # Option 4 -Quit the program
        elif user_input == "4":
            print("Good bye, Have a wonderful day!")
            # use break function finished the loop execution
            break
        
        else :
            print("Invalid choice, please try again.")
            # use continue function to continue the loop again
            continue

# Call main function here
print(menu())