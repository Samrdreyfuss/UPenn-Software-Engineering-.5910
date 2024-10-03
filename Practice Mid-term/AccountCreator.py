# https://www.geeksforgeeks.org/python-cross-mapping-of-two-dictionary-value-lists/

from Account import *
from AccountManager import *


class AccountCreator(object):
    """"A class for loading bank account information from a file, storing it in a dictionary,
    and calculating the account balance.
    """

    # We do not have an __init__ function and will call the default constructor.
    accounts = 'acounts.txt'
    deposits = 'deposits.csv'
    withdrawals = 'withdrawals'

    def init_bank_accounts(self, accounts, deposits, withdrawals):
        '''
        Loads the given 3 files, stores the information for individual bank accounts in a dictionary,
        and calculates the account balance. This function calculates the total balance for each account by taking the
        total deposit amount and subtracting the total withdrawal amount.

        Step 1:
        For the Accounts file, get the information and put it in a bank_accounts dictionary.
        The keys for the dictionary are account numbers as strings, and the values are Account objects
        (objects of the Account class that represent individual bank accounts).

        Accounts file contains information about bank accounts.
        Each row contains an account number, a first name, and a last name, separated by vertical pipe (|).
        Example:
        1|Brandon|Krakowsky

        Step 2:
        For the Deposits file, deposit the given amounts to the given accounts. The accounts to which you're
        depositing are found in the bank_accounts dictionary you created in Step 1.

        Deposits file contains a list of deposits for a given account number.
        Each row contains an account number, and a list of deposit amounts, separated by a comma (,).
        Example:
        1,234.5,6352.89,1,97.60

        Step 3:
        For the Withdrawals file, withdraw the given amounts from the given accounts. The accounts from which
        you're withdrawing are found in the bank_accounts dictionary you created in step 1.

        Withdrawals file contains a list of withdrawals for a given account number.
        Each row contains an account number, and a list of withdrawal amounts, separated by a comma (,).
        Example:
        1,56.3,72.1
        '''

        # step 1:

        with open('accounts.txt', 'r') as account_names:
            lines = account_names.readlines()

        name_accounts = {}
        for name in lines:
            # remove | and replace with comma
            name = name.replace('|', ',')
            # strip white space
            name = name.strip()
            name = name.replace(' ', '')

            # convert the line to a dictionary entry
            split_line = name.split(',')
            # print(split_line[1:])
            # name = [split_line[0]] + split_line[1:]
            name_accounts[split_line[0]] = split_line[1:]

        bank_accounts = {}
        for key, value in name_accounts.items():
            bank_object = Account(key, value[0], value[1])
            bank_accounts[key] = bank_object
            # bank_object.balance = value[2]

        # Step 2: all deposit logic
        with open('deposits.csv', 'r') as deposit_amounts:
            lines = deposit_amounts.readlines()

            deposit_dictionary = {}
            for account in lines:
                # strip white space
                account = account.strip()

                # convert the line to a dictionary entry
                account_split_line = account.split(',')
                account_summation_list = account_split_line[1:]
                account_total = 0
                for deposit in account_summation_list:
                    # convert to float
                    deposit = float(deposit)
                    account_total += deposit
                    account_total = round(account_total, 2)

                    # convert the line to a dictionary entry
                deposit_dictionary[account_split_line[0]] = account_total

        # Step 3: all withdrawn logic
        # all withdrawn logic
        with open('withdrawals.csv', 'r') as withdrawl_amounts:
            lines = withdrawl_amounts.readlines()

            withdrawl_dictionary = {}
            for account in lines:
                # strip white space
                account = account.strip()

                # convert the line to a dictionary entry
                account_split_line = account.split(',')
                account_summation_list = account_split_line[1:]
                account_total = 0
                for withdrawl in account_summation_list:
                    # convert to float
                    withdrawl = float(withdrawl)
                    account_total += withdrawl
                    account_total = round(account_total, 2)

                    # convert the line to a dictionary entry
                withdrawl_dictionary[account_split_line[0]] = account_total

        # subtract the withdrawl dictionary from the deposit dictionary:
        balance_dict = {key: round(deposit_dictionary[key] - withdrawl_dictionary[key], 2) for key in deposit_dictionary
                        if key in withdrawl_dictionary}

        # map balance_dict onto the bank_accounts dictionary and also convert the values into a list
        for key in bank_accounts:
            if key in balance_dict:
                bank_object = bank_accounts[key]
                bank_object.balance = balance_dict[key]

        return bank_accounts



