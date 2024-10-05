from cytoolz import accumulate
from sympy import print_glsl

from Account import *
from AccountCreator import *


class AccountManager(object):
    """"A class for managing account operations.
    """

    # We do not have an __init__ function and will call the default constructor.

    def round_balance(self, bank_accounts, account_number):
        '''Rounds the given amount to two decimal places.
        '''

        account = bank_accounts[account_number]
        account.balance = round(account.balance, 2)

    def get_account(self, bank_accounts, account_number):
        '''Returns the Account object for the given account_number.
        If the account doesn't exist, returns None
        '''

        return bank_accounts.get(account_number)

    def withdraw(self, bank_accounts, account_number, amount):
        '''Withdraws the given amount from the account with the given account_number.
        Rounds the new balance to 2 decimal places.
        If the account doesn't exist, prints a friendly message.
        Raises a RuntimeError if the given amount is greater than the available balance.
        Prints the new balance.
        '''

        account = self.get_account(bank_accounts, account_number)
        if account == None:
            print("Sorry, that account doesn't exist.")
            return
        if (amount > amount.balance):
            raise RuntimeError('Amount greater than available balance')

        account.balance -= amount
        self.round_balance(bank_accounts,account_number)

        print("New balance:", account.balance)

    def deposit(self, bank_accounts, account_number, amount):
        '''Deposits the given amount into the account with the given account_number.
        Rounds the new balance to 2 decimal places.
        If the account doesn't exist, prints a friendly message.
        Prints the new balance.
        '''

        account = self.get_account(bank_accounts,account_number)
        if account == None:
            print("Sorry, that account doesn't exist.")
            return

        account.balance += amount
        self.round_balance(bank_accounts,account_number)

        print('New balance:', account.balance)


    def purchase(self, bank_accounts, account_number, amounts):
        '''Makes a purchase with the total of the given amounts from the account with the given account_number.
        If the account doesn't exist, prints a friendly message.
        Calculates the total purchase amount based on the sum of the given amounts, plus (6%) sales tax.
        Raises a RuntimeError if the total purchase amount is greater than the available balance.
        Prints the new balance.
        '''

        account = self.get_account(bank_accounts,account_number)
        if account == None:
            print("Sorry, that account doesn't exist.")
            return

        tot_withdrawl_amount = sum(amounts)

        # calculate and add 6% sales tax
        tot_withdrawl_amount += self.calculate_sales_tax(tot_withdrawl_amount)

        self.withdraw(bank_accounts,account_number, tot_withdrawl_amount)


    @staticmethod
    def calculate_sales_tax(amount):
        '''Calculates and returns a 6% sales tax for the given amount.'''

        return amount * .06

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

        # check given sort_type

        if sort_type not in ['account_number','first_name','last_name','balance']:
            print("Unexpected inputs, please input 'account_number','first_name','last_name', or ")

        # get list of tuples
        bank_accounts_items = list(bank_accounts.items())

        # set reverse
        reverse = False if sort_direction == 'asc' else True

        # Hint: Check given sort_type, if its not valid return none

        # Hint: Get list of tuples from bank_accounts

        # Hint: Sort items based on sort_type and given sort_direction if given sort_type is account_number, sort on account_number casted to int, otherwise, sort on specific attribute using getattr

        # Hint: Return a sorted list of tuples

        if sort_type == "account_number":
            sorted_items = sorted(bank_accounts.items(), key=lambda  item:
                                        int(item[0]), reverse=reverse)

        else:
            sorted_items = sorted(bank_accounts_items,key=lambda item getattr(item[1],sort_type),reverse=reverse)

        return sorted_items

    def export_statement(self, bank_accounts, account_number, output_file):
        '''Exports the given account information to the given output file in the following format:

        First Name: Huize
        Last Name: Huang
        Balance: 34.57
        '''

        account = self.get_account(bank_accounts,account_number)
        if account == None:
            print("Sorry, that account doesn't exist.")
            return

        # format account info
        account_info_str = 'First Name: ' + account.first_name + '\n'
        account_info_str = 'Last Name: ' + account.last_name + '\n'
        account_info_str = 'Balance: ' + str(account.balance) + '\n'

        fout = open(output_file,'w')
        fout.write(account_info_str)
        fout.close()
