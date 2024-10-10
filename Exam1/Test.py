from ExpensesLoader import *
from ExpensesManager import *

test = ExpensesLoader()

expenses = {}

test.import_expenses(expenses, 'Expenses.txt')

test.import_expenses(expenses, 'expenses_2.txt')


expense_manger = ExpensesManager()


expense_manger.add_expense(expenses, 'coffee', 1)




