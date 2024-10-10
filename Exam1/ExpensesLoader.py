from pandas.core.config_init import pc_max_info_rows_doc

from Expense import *


class ExpensesLoader(object):
    """A class for loading expenses from a file.
    """

    # We do not have an __init__ function and will call the default constructor

    def import_expenses(self, expenses, file):
        """Reads data from the given file and stores the expenses in the given expenses dictionary, where the expense
        type is the key and the value is an Expense object with the parameters expense type and total amount for that
        expense type.

        The same expense type may appear multiple times in the given file, so add all the amounts for the same
        expense types.

        Ignore expenses with missing amounts. If a line contains both an expense type and an expense amount,
        they will be separated by a colon (:).

        You can assume that if they exist, expense types are one-word strings and the amounts are numerical and can
        be casted to a float data type.

        Strip any whitespace before or after the expense types and amounts. Blank lines should be ignored.

        Expenses are case-sensitive. "coffee" is different from "Coffee".

        This method will be called twice in the main function in expenses.py with the same dictionary, but different
        files.

        This method doesn’t return anything.  Rather, it updates the given expenses dictionary based
        on the expenses in the given file.

        For example, after loading the expenses from the file, the expenses dictionary should look like
        this: {'food': Expense('food', 5.00), 'coffee': Expense('coffee', 12.40),
               'rent': Expense('rent', 825.00), 'clothes': Expense('clothes', 45.00),
               'entertainment': Expense('entertainment', 135.62), 'music': Expense('music', 324.00),
               'family': Expense('family', 32.45)}

        Note: You are not expected to handle negative numbers in your code
        """

        # The expenses dictionary datastructure is passes as argument so no need to define here

        # call helper function (within import expenses class) which reads the expense file lines to a single string
        expense_lines = self.init_file(file)

        # loop through each line in account_lines list
        for line in expense_lines:

            # strip \n and empty space
            line = line.strip()

            # get rid of spaces via replace method
            expense_info = line.replace(' ','')


            # split the line by semicolon
            expense_info = expense_info.split(':')

            try:
                if expense_info[1] == '':
                    continue

                elif expense_info[0] == '':
                    continue
            except:
                continue

            # define expense category as
            expense_category = expense_info[0].strip()

            # get expense amount and convert to float
            expense_amount = float(expense_info[1].strip())



            # call object
            
            # create an instance of account and store it in a bank_accounts dict:
            if expense_category in expenses.keys():
                expense_object = expenses[expense_category]
                expense_object.add_amount(expense_amount)

            else:
                #expense_object = expenses[expense_category]
                # need to add_expense
                expenses[expense_category] = Expense(expense_category, expense_amount)



        #print(expenses)


    def init_file(self, file):
        '''
        Loads the given file and returns the lines as a list
        Args:
            file:

        Returns:
        '''

        f = open(file, 'r')
        lines = f.readlines()
        f.close

        return lines
