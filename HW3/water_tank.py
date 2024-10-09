"""
Name: Sam Dreyfuss
PennID: 16863023

I worked alone on this assignment, but referenced the following additional websites to further improve my understanding
several topics which I implemented in my program

https://www.w3schools.com/python/python_lambda.asp
https://www.geeksforgeeks.org/underscore-_-python/
https://discuss.python.org/t/why-do-my-lists-get-modified-when-passed-to-a-function/5036
https://www.w3schools.com/python/ref_string_isdigit.asp

"""

# import statements
import random
from random import shuffle


def get_user_input(question):
    """
    Functionality:
    Prompt the user with the given question and process the input.
    ○ Return the post-processed user input.
    ○ Remove leading and trailing whitespaces.
       ○ If the length of the user input after removing leading and trailing whitespaces is 0, reprompt.
       ○ If the input is a number, cast and return an integer type.
       ○ If the input is a power card, return the power card as an uppercase string.
       ○ If the input is any other string, return the string as a lowercase string.

    Arguments:
    Question: string - the user is asked to answer via an input function

    Return:
    string: a processed answer from user to ensure correct formatting and usability by the program
    """

    # check user input to ensure the correct values have been entered for this program (ex: no missing values, )
    while True:
        try:
            post_processed_user_input = input(question).strip()

            # If length of the user input after removing leading and trailing whitespaces is 0 reprompt.
            if len(post_processed_user_input) == 0:
                raise ValueError

            # If input is a number cast and return an integer type.
            if post_processed_user_input.isdigit():
                return int(post_processed_user_input)

            # If input is a power card return the card as an uppercase string.
            if post_processed_user_input.lower() in ('soh', 'dot', 'dmt'):
                return post_processed_user_input.upper()

            # If input is any other string return value as a lowercase string.
            if isinstance(post_processed_user_input, str):
                return post_processed_user_input.lower()


        except ValueError:
            print("You didn't enter a valid input")


def setup_water_cards():
    """
    Functionality:
    The setup_water_cards functions creates a shuffled list of water cards with the following values and quantities:
       Value Quantity of Cards
       1      30
       5      15
       10     8

    Arguments:
    None

    Returns:
    list: a shuffled water cards list of integers.
    """
    # create an empty list to add to
    shuffled_list_of_water_cards = []

    # create list of tuples which will be used to define each value/quantity pair of cards
    value_quantity_cards_tuples = [(1, 30), (5, 15), (10, 8)]

    # loop through each tuple and use tuple values to create the specific number of values/cards
    # upon each loop, extend the shuffled_list_of_water_cards list with the newly created list, then shuffle
    for value, q_of_cards in value_quantity_cards_tuples:
        shuffled_list_of_water_cards.extend([value for _ in range(q_of_cards)])
    shuffle(shuffled_list_of_water_cards)
    return shuffled_list_of_water_cards


def setup_power_cards():
    """
    Functionality:
    ● Create a shuffled list of power cards with the following values and quantities:

    Value Quantity of Cards Description
    SOH 10 Steal half opponent’s tank value. If the
    opponent’s tank value is an odd integer, it will
    truncate the decimal value (Example: ½ of 5 is 2)
    Hint: You may use the cast to int
    DOT 2 Drain opponent’s tank
    DMT 3 Double my tank’s value.

    ● Hint: Use the shuffle function from the random module.
    ● Return the power cards as a list of strings.

    Arguments:
    None

    Return:
    list: a shuffled power cards list of strings.
    """
    # create an empty list to add to
    shuffled_list_of_power_cards = []

    # create list of tuples which will be used to define each value/quantity pair of cards
    value_quantity_cards_tuples = [('SOH', 10), ('DOT', 2), ('DMT', 3)]

    # loop through each tuple and use tuple values to create the specific number of values/cards
    # upon each loop, extend the shuffled_list_of_power_cards list with the newly created list, then shuffle
    for value, q_of_cards in value_quantity_cards_tuples:
        shuffled_list_of_power_cards.extend([value for _ in range(q_of_cards)])
    shuffle(shuffled_list_of_power_cards)
    return shuffled_list_of_power_cards


def setup_cards():
    """
    Functionality:
    The setup_cards function creates
    ● Set up both the water card and power card piles as described in the setup_water_cards
        and setup_power_cards functions.
    ● Return a 2-tuple containing the water cards pile and the power cards pile, respectively.
    (Each pile should be represented by a list.)

    Arguments:
    None

    Return:
    Tuple: combined water and power cards lists
    """
    # call water cards and power cards functions
    water_cards = setup_water_cards()
    power_cards = setup_power_cards()

    # create tuple from both lists
    cards_list = (water_cards, power_cards)

    # return tuple
    return cards_list


def get_card_from_pile(pile, index):
    """
    Functionality:
    ● Removes the entry at the specified index of the given pile (water or power) and
    modifies the pile by reference.
    ● This function returns the entry at the specified index. HINT: Use the pop function

    Arguments:
    pile: list of cards (either water or power)
    index: index value to be used to pop card from pile

    Returns:
    entry: either int or str card held in the card pile
    """
    # pop specific index off pile of cards
    entry = pile.pop(index)
    return entry


def arrange_cards(cards_list):
    """
    Functionality:
    ● Arrange the players cards such that:
    ○ The first three indices are water cards, sorted in ascending order.
    ○ The last two indices are power cards, sorted in alphabetical order.
    ● This function doesn’t return anything.

    Argument:
    cards_list: list of cards to be shuffled

    Returns:
    None
    """
    # sort all cards so that numbers are sorted first then letters without having a return statment
    cards_list.sort(key=lambda x: (isinstance(x, str), x))


def deal_cards(water_cards_pile, power_cards_pile):
    """
    Functionality:
    ● Deals cards to player 1 and player 2. Each player would get 3 water cards and 2 power
    cards. Then, call the arrange_cards function to arrange the cards.
    ● When dealing, alternately take off a card from the first entry in the pile. Example:

        Initially, the water and pile would be:
        water_pile = [5, 1, 1, 1, 1, 5, 1, 10, 1, 10, 5, 1, 1, 5, 1 , ...]
        power_pile = ['SOH', 'SOH', 'DOT', 'DMT', 'DOT', 'SOH', 'SOH', …]
        After dealing, player 1 and 2 would have the following cards in their hand:
        player_1_cards = [5, 1, 1, 'SOH', 'DOT'] ⇒ arrange to [1, 1, 5, 'DOT', 'SOH']
        player_2_cards = [1, 1, 5, 'SOH, 'DMT'] ⇒ arrange to [1, 1, 5, 'DMT', 'SOH’]
        Then, the piles would now be reduced to:
        water_pile = [1, 10, 1, 10, 5, 1, 1, 5, 1 , ...]
        power_pile = ['DOT', 'SOH', 'SOH', …]

    ● Return a 2-tuple containing the player 1’s hand and player 2’s hand, respectively. (Each
    hand should be represented by a list.)

    Arguments:
    water_cards_pile: list of water cards
    power_cards_pile: list of power cards

    Return:
    Tuple: player_1_cards, player_2_cards - each player's hand is represented by a list
    """

    # For Player 1: pop off 3 alternating values of the water cards and combine those values
    water_cards_pile_val_1 = water_cards_pile.pop(0)
    water_cards_pile_val_2 = water_cards_pile.pop(1)
    water_cards_pile_val_3 = water_cards_pile.pop(0)
    player_1_water_values = [water_cards_pile_val_1, water_cards_pile_val_2, water_cards_pile_val_3]

    # For Player 1: pop off the 2 alternating values of the power cards and combine those values
    power_cards_pile_val_1 = power_cards_pile.pop(0)
    power_cards_pile_val_2 = power_cards_pile.pop(1)
    player_1_power_values = [power_cards_pile_val_1, power_cards_pile_val_2]
    player_1_cards = player_1_water_values + player_1_power_values

    # For Player 2: pop off the 3 alternating values of the water cards and combine those values
    water_cards_pile_val_1 = water_cards_pile.pop(0)
    water_cards_pile_val_2 = water_cards_pile.pop(0)
    water_cards_pile_val_3 = water_cards_pile.pop(0)
    player_2_water_values = [water_cards_pile_val_1, water_cards_pile_val_2, water_cards_pile_val_3]

    # For Player 2: pop off the 2 alternating values of the power cards and combine those values
    power_cards_pile_val_1 = power_cards_pile.pop(0)
    power_cards_pile_val_2 = power_cards_pile.pop(0)
    player_2_power_values = [power_cards_pile_val_1, power_cards_pile_val_2]
    player_2_cards = player_2_water_values + player_2_power_values

    # arrange both both players cards
    arrange_cards(player_1_cards)
    arrange_cards(player_2_cards)
    return (player_1_cards, player_2_cards)


def apply_overflow(tank_level):
    """
    Functionality:
    ● If necessary, apply the overflow rule discussed in the “About the Assignment” section
    of this assignment.
        remaining water = maximum fill value - overflow
    ● Return the tank level. If no overflow occurred, this is just the starting tank level.

    Arguments:
    tank_level: int - the level of each opponents water tank

    Return:
    int: the modified tank level if the player goes over 80
    """
    # the logic below uses the remaining water = maximum fill value - overflow to return the remaining tank level if
    # the tank level goes over 80
    if tank_level > 80:
        tank_level = 80 - (tank_level - 80)
        # tank_level = int(tank_level)
    return tank_level


def use_card(player_tank, card_to_use, player_cards, opponent_tank):
    """
    Functionality:
    ● Get that card from the player’s hand, and update the tank level based on the card that
    was used. This does not include drawing a replacement card, so after using the card,
    the player_cards size will only be 4 cards.
    ● Apply overflow if necessary.
    ● Return a 2-tuple containing the player’s tank and the opponent’s tank, respectively.

    Arguments:
    player_tank: int - the player's current tank level
    card_to_use: int or str - the card to use to analyze what will happend to the player tank and opponent
    player_cards: list - players cards
    opponent_tank: int - opponents tank

    Return:
    tuple of potentially modified player_tank and opponent_tank
    """

    # the below logic while dertermine if the users response was a number or a string.
    # if a int is used that number is added to the humans tank

    if type(card_to_use) == int:
        player_tank += card_to_use
    # the below logic defines the "special actions" when a power card is used:
    else:
        # steal half of opponents tank:
        if card_to_use == 'SOH':
            half_of_opponent_tank = round(opponent_tank / 2)
            player_tank += half_of_opponent_tank
            opponent_tank -= half_of_opponent_tank
        # drain opponents tank
        elif card_to_use == 'DOT':
            opponent_tank = 0
        # double humans tank
        elif card_to_use == 'DMT':
            player_tank = player_tank * 2

    # call discard function or simply remove card used
    player_cards.remove(card_to_use)

    # apply overflow:
    player_tank = apply_overflow(player_tank)
    return (player_tank, opponent_tank)


def use_card_simulation(player_tank_simulation, card_to_use, player_cards, opponent_tank_simulation):
    """
    Functionality:
    The function is a replication of the use_card function, but is used purely for simulation to understand the players
    tank level after analyzing each card to see if there is a winning card within the hand. It does not alter the players hand

    ● Get that card from the player’s hand, and update the tank level based on the card that
    was used.
    ● Simulate overflow if necessary.
    ● Return a 2-tuple containing the player’s tank and the opponent’s tank, respectively.

    Arguments:
    player_tank_simulation: int - the player's current tank level
    card_to_use: int or str - the card to use to analyze what will happend to the player tank and opponent
    player_cards: list - players cards
    opponent_tank_simulation: int - opponents tank

    Return:
    tuple of potentially modified player_tank_simulation and opponent_tank_simulation
    """

    # the below logic while dertermining if the users response was a number or a string.
    # if a int is used that number is added to the humans tank

    if type(card_to_use) == int:
        player_tank_simulation += card_to_use
    # the below logic defines the "special actions" when a power card is used:
    else:
        # steal half of opponents tank:
        if card_to_use == 'SOH':
            half_of_opponent_tank = round(opponent_tank_simulation / 2)
            player_tank_simulation += half_of_opponent_tank
            opponent_tank_simulation -= half_of_opponent_tank
        # drain opponents tank
        elif card_to_use == 'DOT':
            opponent_tank_simulation = 0
        # double humans tank
        else:
            player_tank_simulation = player_tank_simulation * 2

    # apply overflow:
    player_tank_simulation = apply_overflow(player_tank_simulation)
    return (player_tank_simulation, opponent_tank_simulation)


def discard_card(card_to_discard, player_cards, water_cards_pile, power_cards_pile):
    """
    Funtionality:
    ● Discard the given card from the player’s hand and return it to the bottom of the
    appropriate pile. (Water cards should go in the water card pile and power cards should
    go in the power card pile.) The bottom of the pile is the last index in the list.
    ● Same as use_card(), this function does not include drawing a replacement card, so after
    calling this function, the player_cards size will only be 4 cards.
    ● This function does not return anything.

    Arguments:
    player_tank: int - the player's current tank level
    card_to_discard: int or str - the card to discard
    player_cards: list - players cards
    opponent_tank: int - opponents tank level

    Return:
    None
    """
    # remove discarded card from
    player_cards.remove(card_to_discard)

    # the logic below determines which water or cards pile to remove from
    if type(card_to_discard) == int:
        water_cards_pile.append(card_to_discard)
    else:
        power_cards_pile.append(card_to_discard)


def filled_tank(tank):
    """
    Functionality:
    ● Determine if the tank level is between the maximum and minimum fill values
    (inclusive).
    ● Return a boolean representing whether the tank is filled.
    ○ This will be True if the tank is filled.

    Arguments:
    tank: int - the tank water level

    Return:
    boolean: true or false
    """
    # check tank size to confirm the tank is between 75 & 80
    if tank >= 75 and tank <= 80:
        filled_tank = True
    else:
        filled_tank = False
    return filled_tank


def check_pile(pile, pile_type):
    """
    Functionality:
    ● Checks if the given pile is empty. If so, call the pile’s setup function to replenish the pile.
    ● pile_type is a string to determine what type of pile you are checking (“water” or
    “power”)
    ● This function does not return anything.

    Arguments:
    pile: list of cards (either water or power)
    index: index value to be used to pop card from pile

    Return:
    None
    """
    # check to confirm pile type (str = power, and int = water) then check if length is 0/empty, subsequently
    # call setup cards function if list is empty
    if pile_type == "water":
        if len(pile) == 0:
            pile[:] = setup_water_cards()

    elif pile_type == "power":
        if len(pile) == 0:
            pile[:] = setup_power_cards()


def human_play(human_tank, human_cards, water_cards_pile, power_cards_pile, opponent_tank):
    """
    Functionality:
    ● Show the human player’s water level and then the computer player’s water level.
    ● Show the human player their hand and ask them if they want to use or discard a card. If
    the human player enters an invalid answer, reprompt until a valid answer is entered.
    ● Carry out the human’s turn based on the action they have chosen (based on user input).
    Be sure to use the get_user_input function.
    ● Print the card the human player uses or discards. If the human player enters a card to
    use or discard which is not in their hand, reprompt until a valid card is entered.
    ● Remember to handle potential overflows.
    ● Once the human has used or discarded a card, draw a new card of the same type they
    just used/discarded.
    ● Make sure that the human’s hand is still properly arranged after adding the new card.
    ● Return a 2-tuple containing the human’s tank level and the computer’s tank level,
    respectively.

    Arguments:
    human_tank: int - the water tank of the human
    human_cards: list - the 5 cards for the human player in an [int,int,int,str, str] format
    water_cards_pile: list - the list of water cards from the water card pile
    power_cards_pile list - the list of power cards from the power card pile
    opponent_tank: int - the water tank of the human

    Return:
    tuple: human_tank, opponent_tank
    """
    # display human water level
    print(f"=== Human Player's turn ===\nYour water level is: {human_tank}")
    # display computer water level
    print(f"Computer's water level is at: {opponent_tank}")
    # display human's card
    print("Your cards are: ", end=" ")
    # arrange_cards(human_cards)
    print(human_cards)

    # ask user if they would like to use/discard a card
    question_1 = 'Do you want to use a card or discard a card? (u / d): '
    while True:
        answer_1 = get_user_input(question_1)
        if answer_1 == 'd' or answer_1 == 'u':
            break
        else:
            print("Invalid input. Please enter 'u' to use or 'd' to discard a card")

    # if the decision is d or discard, follow the subsequnt logic
    if answer_1 == 'd':
        while True:
            try:
                question_2 = 'Which card do you want to discard?: '
                card_to_discard = get_user_input(question_2)

                # confirm card is held in human "hand"
                if card_to_discard in human_cards:
                    break

                else:
                    raise ValueError

            except ValueError:
                print('You do not hold that card. Please try again.')
                card_to_discard = get_user_input(question_2)

        print(f'Discarding card: {card_to_discard}')

        # call discard function
        discard_card(card_to_discard, human_cards, water_cards_pile, power_cards_pile)

        # draw new card from either water or power pile to replace discarded card in players "hand":
        if type(card_to_discard) == int:
            new_card_pulled_from_pile = get_card_from_pile(water_cards_pile, 0)
        else:
            new_card_pulled_from_pile = get_card_from_pile(power_cards_pile, 0)

        print(f'New card pulled: {new_card_pulled_from_pile}')
        human_cards.append(new_card_pulled_from_pile)

        # display human's water level
        print(f"Your water level is at: {human_tank}")

        # display computer water level
        print(f"Computer's water level is at: {opponent_tank}")

        # display human's card after card has been redrawn
        print(f"Your cards are now: ", end="")
        arrange_cards(human_cards)
        print()

    # if the decision is 'u' or 'use':
    elif answer_1 == 'u':
        while True:
            try:
                question_2 = 'Which card do you want to use?: '
                card_to_use = get_user_input(question_2)

                if card_to_use in human_cards:
                    break

                else:
                    raise ValueError

            except ValueError:
                print('You do not hold that card. Please try again.')

        print(f'Playing with card {card_to_use}')

        # call the use card function
        human_tank, opponent_tank = use_card(human_tank, card_to_use, human_cards, opponent_tank)

        # logic to redraw water or power pile if deck is empty (for either water or power pile):
        if len(water_cards_pile) == 0:
            water_cards_pile, power_cards_pile = setup_cards()
        if len(power_cards_pile) == 0:
            water_cards_pile, power_cards_pile = setup_cards()

        # draw new card from either water or power pile to replace card used in players "hand":
        if type(card_to_use) == int:
            new_card_pulled_from_pile = get_card_from_pile(water_cards_pile, 0)

        else:
            new_card_pulled_from_pile = get_card_from_pile(power_cards_pile, 0)

        # check if overflow occured:
        human_tank = apply_overflow(human_tank)

        print(f'New card pulled: {new_card_pulled_from_pile}')
        human_cards.append(new_card_pulled_from_pile)

        # display human's water level
        print(f"Your water level is at: {human_tank}")

        # display computer water level
        print(f"Computer's water level is at: {opponent_tank}")

        # display human's card after card has been redrawn
        # print(f"Your cards are now: ", end="")
        arrange_cards(human_cards)
        print(f"Your cards are now: {human_cards}")
    return (human_tank, opponent_tank)


def computer_play(computer_tank, computer_cards, water_cards_pile, power_cards_pile, opponent_tank):
    """
    Functionality:
    ● This is the function where you can write the computer’s strategy.
    ● You are supposed to be somewhat creative here, but make sure your code is
    deterministic (not random).
    ● The computer’s strategy should consider all of its cards when playing. For example, you
    should not have a strategy where the computer always plays the first water card or the
    first power card.
    ● The computer should not “cheat.” They should not be able to see any cards from the
    human’s hand, the water card pile, or power card pile. When they draw a card, they
    should only see that card and no cards from the rest of the water or power card pile.
    ● This function should carry out the computer’s turn based on the action that the
    computer chooses.
    ● Remember to handle potential overflows.
    ● Print the card the computer player uses or discards.
    ● Once the computer has used or discarded a card, give them a new card of the same
    type they just used/discarded.
    ● Make sure that the computer’s hand is still properly arranged after adding the new card.
    ● Return a 2-tuple containing the computer’s tank level and the human’s tank level,
    respectively.

    Arguments:
    computer_tank: int - the water tank of the computer
    computer_cards: list - the 5 cards for the computer player in an [int,int,int,str, str] format
    water_cards_pile: list - the list of water cards from the water card pile
    power_cards_pile list - the list of power cards from the power card pile
    opponent_tank: int - the water tank of the human

    Return:
    tuple: computer_tank, opponent_tank
    """
    # display human water level
    print(f"=== Computer Player's turn ===\nComputer water level is: {computer_tank}")
    # display human water level
    print(f"You water level is at: {opponent_tank}")

    # remove duplicates in hand via set method to reduce O notation/reduce redundance iteration of logic
    unique_hand_list = list(set(computer_cards))

    # define empty str and int lists
    int_list = []
    str_list = []

    # break up unique values in had into int and str lists
    for value in unique_hand_list:
        if type(value) == int:
            int_list.append(value)
        else:
            str_list.append(value)

    # reverse int list so that the max value is at the zero index of list
    int_list.sort(reverse=True)

    # check each water value to determine if there's an optimal move realtive to using a power care
    simulated_take_half = 0
    simulated_drain_opponents_tank = 0
    simulated_double_current_tank = 0
    decision_max_value_from_last_loop = 0
    optimal_choice_from_last_loop = ''
    total_optimal_decision = 0

    # check each value in int_list via for loop
    for value in int_list:

        # set optimal choice for loop to blank:
        optimal_choice_in_loop = ''

        # simulate options in power cards by checking outcome of each potential power card for each water card value
        if 'SOH' in str_list:
            simulated_take_half = opponent_tank / 2

        # only execute the following logic when the max value in the list is 1 (a simulated_drain_opponents_tank
        # value of 2 is chosen to prioritze this option over other water values of 1)
        if 'DOT' in str_list:
            if value == 1 and opponent_tank > computer_tank:
                simulated_drain_opponents_tank = 2

        if 'DMT' in str_list:
            simulated_double_current_tank = computer_tank

        # combine options into list:
        options_to_choose_from = [value, simulated_take_half, simulated_drain_opponents_tank,
                                  simulated_double_current_tank]

        # Determine which value is maximum
        max_value = max(options_to_choose_from)

        # determine which index the maximum value lies on
        optimal_index = options_to_choose_from.index(max_value)

        # return the hand value which would be the optimal decision on each loop
        if optimal_index == 0:
            optimal_choice_in_loop = value
        elif optimal_index == 1:
            optimal_choice_in_loop = 'SOH'
        elif optimal_index == 2:
            optimal_choice_in_loop = 'DOT'
        elif optimal_index == 3:
            optimal_choice_in_loop = 'DMT'

        # because draining the opponents tank wont actually add anything to our tank, set it back to zero for comparison
        simulated_drain_opponents_tank = 0

        # check if optimal choice would cause an overflow and apply if it does call apply overflow
        # function otherwise monitor highest card value, optimal decision and optimal choice on each loop
        if computer_tank + max_value > 80:
            computer_tank = apply_overflow(computer_tank)

        else:
            if max_value > decision_max_value_from_last_loop:
                decision_max_value_from_last_loop = max_value
                total_optimal_decision = optimal_choice_in_loop
                optimal_choice_from_last_loop = optimal_choice_in_loop
            else:
                total_optimal_decision = optimal_choice_from_last_loop

    # then check to see if any of the cards are winning cards (resulting in computer tank filling to between 75-80)
    for card in computer_cards:
        computer_tank_win_check, opponent_tank_win_check = use_card_simulation(computer_tank, card, computer_cards,
                                                                               opponent_tank)
        if 75 <= computer_tank_win_check <= 80:
            total_optimal_decision = card

    # call the use card function
    computer_tank, opponent_tank = use_card(computer_tank, total_optimal_decision, computer_cards, opponent_tank)

    # draw new card from either water or power pile to replace card used in players "hand":
    if type(total_optimal_decision) == int:
        new_card_pulled_from_pile = get_card_from_pile(water_cards_pile, 0)
    else:
        new_card_pulled_from_pile = get_card_from_pile(power_cards_pile, 0)

    print('Computer playing with card: ', total_optimal_decision)

    # sort cards
    computer_cards.append(new_card_pulled_from_pile)

    # print out it's decision and both tank levels
    print(f"The Computer's water level is now at: {computer_tank}")
    print(f"Your water level is now at: {opponent_tank}")
    arrange_cards(computer_cards)

    return (computer_tank, opponent_tank)


def welcome_and_determine_first_move():
    """
    This function welcomes the user to the Water tank game and provides a brief description of the game, wishes the player luck,
    then uses a rantint function to determine if the human or the computer moves first

    Arguments: None

    Returns:
    first_move
    """
    # print welcome message
    print('Welcome to the WATER TANK game and play against the computer!',
          '\nThe first player to fill their tank wins the game.', '\nGood luck!')
    print()
    # use randint function to determine who moves first (human or computer)
    first_move_boolean = random.randint(0, 1)

    # classify 1 as human and 0 as computer
    if first_move_boolean == 1:
        first_move = 'Human'
    else:
        first_move = 'Computer'

    # print message
    print(f'The {first_move} Player has been selected to go first.')
    print()
    return first_move


def main():
    # call welcome function to welcome user to the game
    first_move = welcome_and_determine_first_move()
    # set human and computer tank to zero as well as tank variable (which alternates between player)
    human_tank = 0
    computer_tank = 0
    tank = 0

    # setup cards and deal to human and computer
    water_cards_pile, power_cards_pile = setup_cards()
    human_cards, computer_cards = deal_cards(water_cards_pile, power_cards_pile)

    while not filled_tank(tank):

        # switch between players, starting with the "first move" player"
        if first_move == 'Computer':
            # alternate between players and witch first_move and opponent_tank variables
            first_move = 'Human'
            opponent_tank = human_tank
            computer_tank, human_tank = computer_play(computer_tank, computer_cards, water_cards_pile, power_cards_pile,
                                                      opponent_tank)
            tank = computer_tank

            # verify to determine if computer won to switch the name of winner:
            if filled_tank(tank):
                winning_player = 'Computer'
            # print statement for formatting purpose
            print()
        else:
            # alternate between players and witch first_move and opponent_tank variables
            opponent_tank = computer_tank
            first_move = 'Computer'
            human_tank, computer_tank = human_play(human_tank, human_cards, water_cards_pile, power_cards_pile,
                                                   opponent_tank)
            tank = human_tank

            # print space for formatting purpose
            print()

            # verify to determine if human won to switch the name of winner:
            if filled_tank(tank):
                winning_player = 'Human'

    print("=== Game Over ===\n", f"{winning_player} Player Won")


if __name__ == '__main__':
    main()