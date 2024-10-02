


with open('accounts.txt', 'r') as account_names:
    lines = account_names.readlines()

bank_accounts = {}
for name in lines:

    # remove | and replace with comma
    name = name.replace('|', ',')
    # strip white space
    name = name.strip()
    name = name.replace(' ','')

    # convert the line to a dictionary entry
    split_line = name.split(',')
    name = [split_line[0]] + split_line[1:]
    bank_accounts[name[0]] = ', '.join(name[1:])

with open('deposits.csv', 'r') as deposit_amounts:
    lines = deposit_amounts.readlines()
    print(lines)

    deposit_dictionary = {}
    for account in lines:
        # strip white space
        account = account.strip()

        # convert the line to a dictionary entry
        account_split_line = account.split(',')
        account_summation_list = account_split_line[1:]
        account_total = 0
        deposit = 0
        for deposit in account_summation_list:
            deposit = float(deposit)
            account_total += deposit
            account_total = round(account_total,2)
        print(account_total)

            # convert the line to a dictionary entry
            #deposit_dictionary[account_split_line[0]] = ','.join(account_total)

        #print(deposit_dictionary)