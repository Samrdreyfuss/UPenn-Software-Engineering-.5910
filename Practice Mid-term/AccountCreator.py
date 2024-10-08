# https://www.geeksforgeeks.org/python-cross-mapping-of-two-dictionary-value-lists/

from Account import *
from AccountManager import *

class AccountCreator(object):
    """"A class for loading bank account information from a file, storing it in a dictionary,
    and calculating the account balance.
    """

    # We do not have an __init__ function and will call the default constructor.

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

        # create empty dictionary for bank accounts
        bank_accounts = {}

        # call helper function (within account creator class) which reads all ACCOUNTS file lines to a single string
        account_lines = self.init_file(accounts)

        # loop through each line in account_lines list
        for line in account_lines:

            # strip \n and empty space
            line = line.strip()

            # split the line by bar
            account_info = line.split('|')

            # define account_number as
            account_number = account_info[0].strip()

            # get first name
            first_name = account_info[1].strip()

            # get last name
            last_name = account_info[2].strip()

            # create an instance of account and store it in a bank_accounts dict:
            bank_accounts[account_number] = Account(account_number,first_name,last_name)

        # call helper function (within account creator class) which reads all DEPOSIT file lines to a single string
        deposit_lines = self.init_file(deposits)


        # for each line in deposit lines
        for line in deposit_lines:

            # strip out white space
            line = line.strip()

            # split by comma
            deposit_info = line.split(',')

            # get account number
            account_number = deposit_info[0].strip()

            # get list of deposits
            deposit_list = deposit_info[1:]

            # convert list to numeric via list comprehension -> list
            deposit_list = [float(i) for i in deposit_list]

            # get total deposit amount
            tot_deposit_amount = sum(deposit_list)

            # create instance of AccountManager
            account_manager = AccountManager()

            #deposit amount
            account_manager.deposit(bank_accounts, account_number, tot_deposit_amount)

        # load withdrawls file
        withdrawal_lines = self.init_file(withdrawals)

        for line in withdrawal_lines:
            line = line.strip()
            withdrawal_info = line.split(',')
            account_number = withdrawal_info[0].strip()

            # get list of withdrawls
            withdrawal_list = withdrawal_info[1:]

            #get list of withdrawls
            withdrawal_list = [float(i) for i in withdrawal_list]

            # get total withdrawl amount:
            tot_withdrawl_amount = sum(withdrawal_list)

            #withdraw amount
            account_manager.withdraw(bank_accounts,account_number,tot_withdrawl_amount)

        return bank_accounts

    def init_file(self,file):
        '''
        Loads the given file and returns the lines as a list
        Args:
            file:

        Returns:

        '''

        f = open(file,'r')
        lines = f.readlines()
        f.close

        return lines



