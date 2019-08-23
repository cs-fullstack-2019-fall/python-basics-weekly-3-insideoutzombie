# Give the user the following options. Once the option that is selected is completed keep asking them until they hit 4 to quit:
#
# ```
# Hello, please choose one of following options:
# 1) Check balance
# 2) Add money to account
# 3) Withdraw money from account
# 4) Quit
# What will you like to do?

user_id = ''
user_pin = 0
# ask user for the correct name on the account
while user_id != 'david':
    user_id = input('Enter the correct account name ')
# ask user for the correct pin to access the account
while user_pin != 1234:
    user_pin = int(input('Enter the correct pin'))
=
# delcare the var to start the journey
user_option = -1
account = 0
# while loop to keep asking over and over
while user_option != 4:
    # print welcome message with prompt instructions
    print(
        'Hello, please choose one of following options:\n'
        '1) Check balance\n'
        '2) Add money to account\n'
        '3) Withdraw money from account\n'
        '4) Quit\n'
    )
    # Get user selection"Check balausernce"
    user_option = int(input('What will you like to do? '))

    # checks user choice
    if user_option == 1: # user selected check Balance
        print('You have $' + str(account) + ' in your account ' + '\n') # print user balance

    elif user_option == 2: # user selected Add money to account
        # Let user add money to account
        account = "" # entered amount
        accountBal = "" # Will hold account amount
        if user_option != 4:
            account = input('How much would you like to deposit? ')
            accountBal += ((accountBal + account) + '\n')
            print('Your account now holds $' + str(account) + ' dollars'+'\n') # print user balance
            user_option = input('Enter "4" to exit to main menu ')

    elif user_option == 3: # user selected Withdraw money from account
        if user_pin != 2134:
            user_pin = int(input('Enter the corrct Pin '))
            # Let user withdraw money to account
            remainder = account # withdraw money from account
            accountWit = 0 # Will hold account amount
            if user_option != 4:
                # input for asking user how much to withdraw
                remainder = int(input('How much money do you want to withdraw? '))
                if(remainder >= accountWit):
                    account = remainder - accountWit
                    # account = accountWit
                    print(account) # print user remainder of balance

            elif(remainder < accountWit):
                print('Insufficient funds')

            user_option = input('Enter "4" to exit to main menu ')


# log off message when user selects 4 as the input
print('Logging Off')
