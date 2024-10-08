# Student Name in Canvas: Sam Dreyfuss
# Penn ID: 16863023
# Did you do this homework on your own (yes / no): yes, but used several outside resources listed below.
# Resources used outside course materials:
# https://www.geeksforgeeks.org/how-to-check-if-variable-is-empty-in-python/
# https://realpython.com/python-pass/
# https://teamtreehouse.com/community/can-you-have-multiple-conditions-in-while-loops

# import statements to be used in program
from random import randint, choice


def print_welcome_and_menu(list_of_flavors, list_of_sizes, list_of_prices):
    """
    The print_welcome_and_menu prints a welcome message as well as lists the current flavors available and their respective
    prices.
    1. Welcome message (Must contain word 'welcome')
    2. Message on what flavors are available in the ice cream store.
        Hint: Loop through the list_of_flavors
    3. Message on how much each size cost.
        Hint: Loop through the list_of_sizes, list_of_prices
        Format should be: Our {size} ice cream is ${price}.
    """
    # print welcome message and display the current ice cream flavors available
    print("Welcome to Penn's Student Run Ice Cream Stand!\n", "\nOur current flavors for today are:")
    for flavor in list_of_flavors:
        print(flavor)
    print()

    # Convert the unique ice cream sizes and ice cream prices into a single list of tuples using a zip function via a for loop
    ice_cream_size_and_price_list_pairs = zip(list_of_sizes, list_of_prices)
    for (size, price) in ice_cream_size_and_price_list_pairs:
        print(f"Our {size} ice cream is ${price}")
    print()


def get_order_qty(customer_name):
    """
    The get_order_qty function asks the customer how many orders of ice cream they want.
    Valid order quantity should be an integer 1-5 inclusive. If outside the range or non-int, re-prompt.
    Hint: When asking for user input, cast it to an integer. If the input cannot be cast-ed to an integer, re-prompt.
    "2.55", "abc", "   ", are a few examples of what should all re-prompt the user.
    Returns: How many orders of ice cream the customer wants.
    """
    # set order_qty to zero so that upon each function call no previous values are saved
    order_qty = 0

    # Ask user for input until the system recieves a correct input (an integer between 1-5), otherwise return error message
    while True:
        try:
            order_qty = int(input(f'Welcome {customer_name}! How many ice creams will you be ordering (1 to 5)?'))
            if order_qty not in range(1, 6):
                raise ValueError
            break

        except ValueError:
            print("You didn't enter a valid number between 1 and 5.")

    return order_qty


def get_ice_cream_flavor(ice_cream_flavors):
    """
    The get_ice_cream_flavor fun Ask the customer 'Which flavor would you like (v/c/s)? '
    Then, processes and cleans the input and returns the equivalent flavor from ice_cream_flavors list.

    Hint:   Use the indices set in the main function for the flavors.
            Call the get_first_letter_of_user_input function to get and process inputs.
            Note: Only the first letter of the input will be considered so an input of 'Cookies and Cream'
            will be considered as 'c' which corresponds to 'Chocolate'.
            Ask again if it is not a valid flavor.
    Returns: String of ice cream flavor picked (e.g "Vanilla")
    """

    # set flavor_picked to blank so that upon each function call no previous values are saved
    flavor_picked = ""

    # Ask user for input which calls the get_first_letter_of_user_input function using the predetermined question below,
    # resulting in the get_first_letter_of_user_input function returning the first letter of the users input.
    # The system will keep asking the user for a correct input until it recieves a correct value (a string being v,c, or s),
    # otherwise return error message then use the index value of from within the ice cream flavors list to return
    # the natural language flavor for each of the v,c, or s input values
    while True:
        try:
            question = 'Which flavor would you like (v/c/s)? '
            flavor = get_first_letter_of_user_input(question)
            if flavor not in ['v', 'c', 's']:
                raise ValueError

            if flavor == 'v':
                flavor_picked = ice_cream_flavors[0]

            elif flavor == 'c':
                flavor_picked = ice_cream_flavors[1]

            elif flavor == 's':
                flavor_picked = ice_cream_flavors[2]
            break


        except ValueError:
            print('The flavor you entered is not a valid input. Please try again.')
    return flavor_picked


def get_ice_cream_size(ice_cream_sizes):
    """
    Ask the customer 'Which size would you like (s/m/l)? '
    Then, processes and cleans the input and returns the equivalent size from ice_cream_sizes list.
    Hint:   Use the indices set in the main function for the sizes.
            Call the get_first_letter_of_user_input function to get and process inputs.
            Note: Only the first letter of the input will be considered so an input of 'Super Large'
            will be considered as 's' which corresponds to 'Small'.
            Ask again if it is not a valid size.
    Returns: String of Size picked (e.g "Small")
    """
    size_picked = ""

    # Ask user for input which calls the get_first_letter_of_user_input function using the predetermined question below,
    # resulting in the get_first_letter_of_user_input function returning the first letter of the users input.
    # The system will keep asking the user for a correct input until it recieves a correct value (a string being s,m, or l),
    # otherwise return error message then use the index value of from within the ice cream sizes list to return
    # the natural language size for each of the s,m, or l input values
    while True:
        try:
            question = 'Which size would you like (s/m/l)? '
            size = get_first_letter_of_user_input(question)
            if size not in ['s', 'm', 'l']:
                raise ValueError

            if size == 's':
                size_picked = ice_cream_sizes[0]

            elif size == 'm':
                size_picked = ice_cream_sizes[1]

            elif size == 'l':
                size_picked = ice_cream_sizes[2]
            break

        except ValueError:
            print('The size you entered is not a valid input. Please try again.')

    return size_picked


def get_ice_cream_order_price(ice_cream_size, ice_cream_prices, ice_cream_sizes):
    """
    Hint:   Use the indices set in the main function for the prices of Small, Medium and Large.
    Returns: The equivalent price of an ice cream size. Example: Returns 4.99 if ice_cream_size is 'Small'
    """
    # Once the user has determined the size of ice cream the would prefer, the below logic references the index value of the
    # ice cream price list to map the natural language size preference with the price for that size and returns that specific
    # price given their size descision
    if ice_cream_size == 'Small':
        price_given_decision = ice_cream_prices[0]

    elif ice_cream_size == 'Medium':
        price_given_decision = ice_cream_prices[1]

    else:
        price_given_decision = ice_cream_prices[2]

    return price_given_decision


def take_customer_order(customer_name, ice_cream_flavors, ice_cream_sizes, ice_cream_prices):
    """
    This function runs when a customer reaches the front of the queue. It should print
    the current customer's name being served, and take their order(s).
    If the customer can pay for their order, returns the amount of revenue from the sale.
    If the customer cancels their order, returns 0.
    Hint: Use other helper functions we required you to write whenever needed here.
    This includes the use of help functions like get_first_letter_of_user_input
    Returns: Amount of Revenue from the sale with customer
    """

    total_bill = 0

    # Print a message "Now serving customer: X" where X is the current customer's name
    print(f'Now serving customer: {customer_name}')

    # Call the get_order_qty and save the value to order_qty
    order_qty = 0
    order_qty = get_order_qty(customer_name)

    # For Each order you need to get a flavor, and size
    for order in range(order_qty):
        # print order number
        print("Order No.:", order + 1)

        # get the ice cream flavor for this order
        ice_cream_flavor_choice = get_ice_cream_flavor(ice_cream_flavors)

        # get the price for this order
        ice_cream_size = get_ice_cream_size(ice_cream_sizes)
        price_for_order = get_ice_cream_order_price(ice_cream_size, ice_cream_prices, ice_cream_sizes)

        # print out ordered size and flavor choice and price
        print(f"You ordered a {ice_cream_size} {ice_cream_flavor_choice} for ${price_for_order}")

        # Update the total_bill
        total_bill += price_for_order

        # Print the details for this order and round to 2 decimals
        #   Hint: See https://www.w3schools.com/python/python_string_formatting.asp for string formatting examples on rounding to 2 decimal places
        txt = f"Your total bill is: ${total_bill:.2f}"

    # Print the customer's total_bill
    print(txt)

    # Once orders are all taken, the customer should be asked if they still want to Pay or Cancel
    # This functionality uses the get_first_letter_of_user_input() and Re-prompts if answer does not start with 'p' or 'c'
    # the total_bill is calculated accordingly pending the pay or cancel order decision
    while True:
        try:
            question = 'Would you like to pay or cancel the order (p/c)? '
            pay_or_cancel_decision = get_first_letter_of_user_input(question)
            if pay_or_cancel_decision not in ['p', 'c']:
                raise ValueError

            if pay_or_cancel_decision == 'p':
                break

            else:
                total_bill = 0
                break

        except ValueError:
            print('The pay/cancel value you entered is not a valid input. Please try again.')

    return total_bill


def get_first_letter_of_user_input(question):
    """
    Takes in a string as its argument, to be used as the question you want the user to be asked.

    Gets input from the user, you must use input() inside this function to pass tests
    Removes whitespace and makes all letters lowercase
    Hint: Use the strip() and lower() functions.
    Note: The question paramter is a string, such as "Which size would you like (s/m/l)?"
    Returns: The first letter of the input the user provides. Ask again if the input is empty.
    """
    first_letter = ""

    # The below logic takes an input question in the form of a string then strips the string of spaces, then converts the
    # string to all lower case values. The subsequent logic confirms there is a value remaining and returns the first value
    # of the word which will be a lowercase value in the original string
    while True:
        answer = input(question).strip().lower()
        if answer:
            return answer[0]


def are_all_customers_served(customer_queue_length):
    """
    If there are no customers in the queue, returns True, and all customers have been served.
    Otherwise, returns False.
    Hint: The parameter customer_queue_length is of type int.
    Returns: True or False
    """
    # if the queue length is greater than 0, all customers are not served (return False), otherwise return true
    if customer_queue_length > 0:
        length = False
    else:
        length = True
    return length


def print_current_status(customers_served, tracking_revenue):
    """
    Prints a message of how many customers have been served and the total sales of the ice cream stand.
    Hint: See https://www.w3schools.com/python/python_string_formatting.asp for string formatting examples on rounding to 2 decimal places
    No Return, only print statements
    """
    # the below logic ensures the tracking revenue variable is only 2 decimal points
    txt = f"and received ${tracking_revenue:.2f} in revenue"
    print(f"We have now served {customers_served} customer(s)", txt)


def print_sales_summary(customers_served, tracking_revenue):
    """
    Takes in the arguments customers_served and tracking_revenue. Prints both
    arguments as strings to let the user know what those values are.
    Output should look something like:
        Total customers served: 3
        Total sales           : $xx.xx
    Hint: See https://www.w3schools.com/python/python_string_formatting.asp for string formatting examples on rounding to 2 decimal places
    No Return, only print statements
    """
    # the below logic ensures the tracking revenue variable is only 2 decimal points
    txt = f"Total Revenue: ${tracking_revenue:.2f}"
    print(f"Customers served: {customers_served}\n", txt)


def random_queue_length():
    """
    Takes no arguments.
    Uses the imported randint function to generate a random integer between 2 and 5 inclusive.
    Hint: See https://www.w3schools.com/python/ref_random_randint.asp
    Returns: The resulting random integer.
    """
    # use the randint function to randomly generate an integer between 2 and 5 inclusive
    rand_int = randint(2, 5)
    return rand_int


def main():
    """
    Lists of available flavors, sizes and prices. DO NOT CHANGE.
    For sizes and prices, we will use the following convention:
    Index 0 for Small
    Index 1 for Medium
    Index 2 for Largecustomer_names
    """
    ice_cream_flavors = ['Vanilla', 'Chocolate', 'Strawberry']
    ice_cream_sizes = ['Small', 'Medium', 'Large']
    ice_cream_prices = [4.99, 7.49, 8.49]

    # List of names of possible customers
    customer_names = ["Alice", "Bob", "Charlie", "Dan", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"]

    program_running = True
    while program_running:
        # set shop to open
        input('Press enter to open the shop! ')
        queue_is_open = True

        # Call the print_welcome_and_menu function with the parameters in the following order -
        #  ice_cream_flavors, ice_cream_sizes, ice_cream_prices
        print_welcome_and_menu(ice_cream_flavors, ice_cream_sizes, ice_cream_prices)

        # set initial values
        tracking_revenue = 0

        # will hold the list of names of the customers in the queue
        customers_in_queue = []
        customers_served = 0

        # TODO: Call the random_queue_length function and save the result to num_of_customers_in_queue
        num_of_customers_in_queue = 0
        num_of_customers_in_queue = random_queue_length()

        # TODO: Print how many customers are in the queue
        print(f'Num of customers in queue: {num_of_customers_in_queue}')
        # print space after above is printed
        print()

        # Call the imported choice function to generate a random name from customer_names.
        # Then, append each name to the end of the customers_in_queue list via a for loop.

        for customer in range(0, num_of_customers_in_queue):
            customers_in_queue.append(choice(customer_names))

        # The total number of customer names added should be equal to num_of_customers_in_queue
        # This is confirmed via the logic below and if not it will generate an error

        try:
            if num_of_customers_in_queue == len(customers_in_queue):
                queue_is_open = True
        except:
            print('There was a "number of customers" error')

        #   Hint: See https://www.w3schools.com/python/ref_random_choice.asp
        #   Note: It is OK to have duplicate names in the queue.

        while queue_is_open:
            # Extract the first customer (index 0) from the customers_in_queue and save it to
            # the current_customer_name variable.
            # After extraction, the customer should now be removed from the customers_in_queue list.
            # Hint: Use the pop function with an index argument
            current_customer_name = ""
            current_customer_name = customers_in_queue.pop(0)

            # Take a customer at the window and update the revenue by calling the take_customer_order function
            revenue_per_customer = take_customer_order(current_customer_name, ice_cream_flavors, ice_cream_sizes,
                                                       ice_cream_prices)
            tracking_revenue += revenue_per_customer

            # Update the customers_served variable
            customers_served += 1

            # Call the print_current_status and print space before and after
            print()
            print_current_status(customers_served, tracking_revenue)
            print()

            # Tall the are_all_customers_served(customer_queue_length) function to check if there are any more
            # customers in the queue.
            customer_queue_length = num_of_customers_in_queue - customers_served

            # If False, continue the loop.
            if are_all_customers_served(customer_queue_length) == False:
                queue_is_open = True

            # If True, call the print_sales_summary(customers_served, tracking_revenue) and close the queue
            else:
                queue_is_open = False
                print_sales_summary(customers_served, tracking_revenue)

        # Ask if you want to open the ice cream stand again "Do you want to open again (y/n)? "
        #  Hint: Use the get_first_letter_of_user_input function
        #  Update the program_running variable if you get a valid answer either 'y' or 'n'
        #  Otherwise, re-prompt until a valid answer is given

        while True:
            try:
                question = 'Do you want to open again (y/n)? '
                open_close_decision = get_first_letter_of_user_input(question)
                if open_close_decision not in ['y', 'n']:
                    raise ValueError

                if open_close_decision == 'y':
                    program_running = True
                    main()

                else:
                    program_running = False
                    break

            except ValueError:
                print('The open/close value you entered is not a valid input. Please try again.')


if __name__ == '__main__':
    main()