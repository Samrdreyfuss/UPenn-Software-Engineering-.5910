from Account import *


class AccountManager(object):
    """"A class for managing account operations.
    """

    # We do not have an __init__ function and will call the default constructor.

    def round_balance(self, bank_accounts, account_number):
        '''Rounds the given amount to two decimal places.
        '''

        # TODO insert your code
        raise NotImplementedError  # remove this line and replace with your code.

    def get_account(self, bank_accounts, account_number):
        '''Returns the Account object for the given account_number.
        If the account doesn't exist, returns None
        '''

        # TODO insert your code
        raise NotImplementedError  # remove this line and replace with your code.

    def withdraw(self, bank_accounts, account_number, amount):
        '''Withdraws the given amount from the account with the given account_number.
        Rounds the new balance to 2 decimal places.
        If the account doesn't exist, prints a friendly message.
        Raises a RuntimeError if the given amount is greater than the available balance.
        Prints the new balance.
        '''
        # TODO insert your code
        raise NotImplementedError  # remove this line and replace with your code.

    def deposit(self, bank_accounts, account_number, amount):
        '''Deposits the given amount into the account with the given account_number.
        Rounds the new balance to 2 decimal places.
        If the account doesn't exist, prints a friendly message.
        Prints the new balance.
        '''

        # TODO insert your code
        raise NotImplementedError  # remove this line and replace with your code.

    def purchase(self, bank_accounts, account_number, amounts):
        '''Makes a purchase with the total of the given amounts from the account with the given account_number.
        If the account doesn't exist, prints a friendly message.
        Calculates the total purchase amount based on the sum of the given amounts, plus (6%) sales tax.
        Raises a RuntimeError if the total purchase amount is greater than the available balance.
        Prints the new balance.
        '''

        # TODO insert your code
        raise NotImplementedError  # remove this line and replace with your code.

    @staticmethod
    def calculate_sales_tax(amount):
        '''Calculates and returns a 6% sales tax for the given amount.'''

        # TODO insert your code
        raise NotImplementedError  # remove this line and replace with your code.

    def sort_accounts(self, bank_accounts, sort_type, sort_direction):
        '''First get the bank_accounts dictionary as a list of tuples. Then based on the specified sort_type
        and sort_direction returns the sorted list of those tuples.

        If the sort_type argument is the string 'account_number', sorts based on
        the account number (e.g. '3', '5') in the given sort_direction (e.g.
        'asc', 'desc').
        Example sorted results based on account_number in ascending order:
        Account Number: 1, First Name: Brandon, Last Name: Krakowsky, Balance: 6557.59
        Account Number: 2, First Name: Chenyun, Last Name: Wei, Balance: 4716.89
        Account Number: 3, First Name: Dingyi, Last Name: Shen, Balance: 4.14

        Otherwise, if the sort_type argument is 'first_name', 'last_name' or
        'balance', sorts based on the associated values (e.g. 'Brandon',
        'Krakowsky', 6557.59) in the given sort direction (e.g. 'asc' or 'desc')
        Example sorted results based on 'balance' in descending order:
        Account Number: 6, First Name: Karishma, Last Name: Jain, Balance: 6700.19
        Account Number: 1, First Name: Brandon, Last Name: Krakowsky, Balance: 6557.59
        Account Number: 2, First Name: Chenyun, Last Name: Wei, Balance: 4716.89
        '''

        # TODO insert your code, we have provided guiding hints for this function

        # Hint: Check given sort_type, if its not valid return none

        # Hint: Get list of tuples from bank_accounts

        # Hint: Sort items based on sort_type and given sort_direction if given sort_type is account_number, sort on account_number casted to int, otherwise, sort on specific attribute using getattr

        # Hint: Return a sorted list of tuples

        raise NotImplementedError  # remove this line and replace with your code.

    def export_statement(self, bank_accounts, account_number, output_file):
        '''Exports the given account information to the given output file in the following format:

        First Name: Huize
        Last Name: Huang
        Balance: 34.57
        '''

        # TODO insert your code
        raise NotImplementedError  # remove this line and replace with your code.