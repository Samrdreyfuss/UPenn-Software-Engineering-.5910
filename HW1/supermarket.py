# import the random module
import random

"""
Name: Sam Dreyfuss
PennID: 16863023

I worked alone on this assignment, but referenced the following additional websites to further improve my understanding of try/accept functionality
when incorporating if/else statements in python to ensure I understood everything correctly:
https://www.w3schools.com/python/python_try_except.asp
https://docs.python.org/3/tutorial/errors.html
https://www.w3schools.com/python/python_functions.asp


The below function allows the user choose and purchase products at a fictitious grocery store. The user decides and enters the quantity they would 
like to purchase of each good and the program records how much money the user has available as money is earned/spent through purchasing lotto tickets,
apples, beans, and sodas.
"""


def grocery_calc():
    # generate a random int from 2 - 10
    winnings = random.randint(2, 10)

    # unit price of a lottery ticket
    constant_lottery_unit_price = 2

    # unit price of an apple
    constant_apple_unit_price = .99

    # unit price of a can of beans
    constant_canned_beans_unit_price = 1.58

    # unit price of a soda
    constant_soda_unit_price = 1.23

    # 1: the user has initial $5 for shopping
    money = 5

    # the user has spent $0 initially
    money_spent = 0

    # the amounts of lottery tickets, apples, cans of beans, and sodas the user has purchased
    lottery_amount, apple_amount, canned_beans_amount, soda_amount = 0, 0, 0, 0

    # 2: print a welcome message to the user which displays a list of products and their unit prices
    print('Welcome to the supermarket! Here is what we have in stock:\n', '-',
          f'Lottery tickets cost ${constant_lottery_unit_price} each\n',
          '-', f'Apples cost ${constant_apple_unit_price} each\n', '-',
          f'Cans of beans cost ${constant_canned_beans_unit_price} each\n', '-',
          f'Sodas cost ${constant_soda_unit_price} each\n')

    # 3: tell user how much money they have available and ask if they want to purchase a lottery ticket
    print(f'You have ${round(money, 2)} available')

    # functionality to allow the user to enter if they would like to purchase a lotto ticket
    lottery_ticket_purchase_decision = input(
        'First, do you want to buy a $2 lottery ticket for a chance at winning $2-$10? (y/n)')

    # the below logic confirms the user entered lottery purchase decision is within the accepeted data format and range (y,Y,n,N) and calculates
    # the net impact to how much money the person has after making a purchase and lottery winning outcome. An error message is given if an incorrect
    # value is entered
    try:

        if lottery_ticket_purchase_decision in ['y', 'Y', 'n', 'N']:

            # conditional logic if a y or Y is entered
            if lottery_ticket_purchase_decision in ['y', 'Y']:

                win_loss_outcome = random.randint(0, 2)
                lottery_amount += 1

                # 2 of 3 outcomes are specified (losses = 0 or 1)
                if win_loss_outcome == 0 or win_loss_outcome == 1:
                    winnings = 0
                    money_spent = 2  # cost of lotto ticket
                    money = money - money_spent
                    print('Sorry! You did not win the lottery. \n')

                # 1 of 3 outcomes are specified (a win = 2)
                # assuming the user would like to purchase, confirm if there's enough money remaining and compute the remaining money after purchase
                else:
                    winnings = winnings
                    money_spent = 2  # cost of lotto ticket
                    money = money + winnings - money_spent
                    print(f'Congrats!, You won ${winnings}! \n')

            # conditional logic if a n or N is entered
            elif lottery_ticket_purchase_decision in ['n', 'N']:
                winnings = 0
                print('No lottery tickets were purchased.  \n')

        else:
            raise ValueError

    except ValueError:
        print('No lottery tickets were purchased.')

    # 4: tell user how much money they have available and ask if they want to purchase apples.
    print(f'You have ${round(money, 2)} available')

    # get user input for apple purchase decision
    apple_purchase_decision = input('Do you want to buy apples? (y/n)')

    # the below logic confirms the user entered apple purchase decision is within the accepted data format and range (y,Y,n,N) and calculates
    # the net impact to their money variable after making a purchase and purchase quanity decision. An error message is given if an incorrect
    # value is entered

    try:

        if apple_purchase_decision in ['y', 'Y', 'n', 'N']:

            # conditional logic if a y or Y is entered
            if apple_purchase_decision in ['y', 'Y']:

                apple_amount = input('How many apple(s) do you want to buy?')
                print(apple_amount)

                # check for data issues:
                try:
                    apple_amount = int(apple_amount)

                    # assuming the user would like to purchase, confirm if there's enough money remaining and compute the remaining money after purchase
                    if money >= apple_amount * constant_apple_unit_price:
                        money_spent = apple_amount * constant_apple_unit_price
                        money = money - money_spent
                        print(
                            f'The user wants to buy {apple_amount} apple(s). This will cost ${round(apple_amount * constant_apple_unit_price, 2)}.')
                        print(f'The user has enough money. {apple_amount} apple(s) purchased \n')

                    else:
                        print(
                            f'The user wants to buy {apple_amount} apple(s). This will cost ${round(apple_amount * constant_apple_unit_price, 2)}.')
                        apple_amount = 0
                        print('Not enough money! No apples were purchased. \n')

                except ValueError:
                    apple_amount = 0
                    print('Integer values only! No apples selected. \n')


            # conditional logic if a n or N is entered
            elif apple_purchase_decision in ['n', 'N']:
                apple_amount = 0
                print('No apples were purchased \n')

        else:
            apple_amount = 0
            raise ValueError

    except ValueError:
        apple_amount = 0
        print('No apples were purchased \n')

    # 5.1: tell user how much money they have available and ask if they want to purchase cans of beans.
    print(f'You have ${round(money, 2)} available')

    # get user input for beans purchase decision
    beans_purchase_decision = input('Do you want to buy can(s) beans? (y/n)')

    # the below logic confirms the user entered beans purchase decision is within the accepeted data format and range (y,Y,n,N) and calculates
    # the net impact to their money variable after making a purchase and purchase quanity decision. An error message is given if an incorrect
    # value is entered

    try:

        if beans_purchase_decision in ['y', 'Y', 'n', 'N']:

            # conditional logic if a y or Y is entered
            if beans_purchase_decision in ['y', 'Y']:

                canned_beans_amount = input('How many cans do you want to buy?')
                print(canned_beans_amount)

                # check for data issues:
                try:
                    canned_beans_amount = int(canned_beans_amount)

                    # assuming the user would like to purchase, confirm if there's enough money remaining and compute the remaining money after purchase
                    if money >= canned_beans_amount * constant_canned_beans_unit_price:
                        money_spent = canned_beans_amount * constant_canned_beans_unit_price
                        money = money - money_spent
                        print(
                            f'The user wants to buy {canned_beans_amount} can(s) of beans. This will cost ${round(canned_beans_amount * constant_canned_beans_unit_price, 2)}.')
                        print(f'The user has enough money. {canned_beans_amount} cans(s) of beans purchased \n')

                    else:
                        print(
                            f'The user wants to buy {canned_beans_amount} can(s) of beans. This will cost ${round(canned_beans_amount * constant_canned_beans_unit_price, 2)}.')
                        canned_beans_amount = 0
                        print('Not enough money! No beans were purchased. \n')

                except ValueError:
                    canned_beans_amount = 0
                    print('Integer values only! No cans of beans selected. \n')


            # conditional logic if a n or N is entered
            elif beans_purchase_decision in ['n', 'N']:
                canned_beans_amount = 0
                print('No beans were purchased. \n')

        else:
            canned_beans_amount = 0
            raise ValueError

    except ValueError:
        canned_beans_amount = 0
        print('No beans were purchased. \n')

    # 5.2: tell user how much money they have available and ask if they want to purchase soda.
    print(f'You have ${round(money, 2)} available')

    # get user input for soda purchase decision
    soda_purchase_decision = input('Do you want to buy soda(s)? (y/n)')

    # the below logic confirms the user entered soda purchase decision is within the accepeted data format and range (y,Y,n,N) and calculates
    # the net impact to their money variable after making a purchase and purchase quanity decision. An error message is given if an incorrect
    # value is entered

    try:

        if soda_purchase_decision in ['y', 'Y', 'n', 'N']:

            # conditional logic if a y or Y is entered
            if soda_purchase_decision in ['y', 'Y']:

                soda_amount = input('How many sodas do you want to buy?')
                print(soda_amount)

                # check for data issues:
                try:
                    soda_amount = int(soda_amount)

                    # assuming the user would like to purchase, confirm if there's enough money remaining and compute the remaining money after purchase
                    if money >= soda_amount * constant_soda_unit_price:
                        money_spent = soda_amount * constant_soda_unit_price
                        money = money - money_spent
                        print(
                            f'The user wants to buy {soda_amount} can(s) of soda. This will cost ${round(soda_amount * constant_soda_unit_price, 2)}.')
                        print(f'The user has enough money. {soda_amount} cans(s) purchased. \n')

                    else:
                        print(
                            f'The user wants to buy {soda_amount} can(s) of soda. This will cost ${round(soda_amount * constant_soda_unit_price, 2)}.')
                        soda_amount = 0
                        print('Not enough money! No sodas were purchased. \n')

                except ValueError:
                    print('Integer values only! No cans of soda selected. \n')
                    soda_amount = 0
                    # print(f'The user wants to buy {soda_amount} can(s) of soda. This will cost ${round(0 * constant_soda_unit_price,2)}.')

            # conditional logic if a n or N is entered
            elif soda_purchase_decision in ['n', 'N']:
                print('No sodas were purchased. \n')

        else:
            soda_amount = 0
            raise ValueError

    except ValueError:
        soda_amount = 0
        print('No sodas were purchased. \n')

    # provide a summary of how much money remains, out come of lottery, and the amount of each item purchased

    print(f'Money left: ${round(money, 2)}')
    print(f'Lottery Ticket(s) purchased: {lottery_amount}')
    print(f'Lottery winnings: ${winnings}')
    print(f'Apple(s) purchased: {apple_amount}')
    print(f'Can(s) of beans purchased: {canned_beans_amount}')
    print(f'Soda(s) purchased: {soda_amount}')
    print('Good bye!')


grocery_calc()