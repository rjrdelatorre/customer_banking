# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account
from savings_account import create_savings_account

def validate_type(value, data_type):
    ''' This function validates the desired data types for user-entered values
            - value: The user-entered value of untested type
            - data_type: The desired data type (e.g. float)
    '''
    try:
        # we need to check for float in int, so let's perform our check dynamically
        type_functions = {'float': float, 'int': int}
        return type_functions[data_type](value)
    except ValueError:
        # tell the user which element had a problem
        print(f"Invalid value: {value}. Please enter a valid {data_type}.")
        if data_type == 'float':
            print("Example: 5.01")
        elif data_type == 'int':
            print("Example: 5")
        return False
    else:
        # there was some other problem, so let's just assume a failure
        return False

def collect_user_input(account_type):
    '''
        # Prompt the user to set the savings balance, interest rate, and months for an account.
            - Test whether the user input is of the correct type
                - balance and interest_rate: float
                - months: int
            - We'll use account_type for the prompt message. The 2 valid options
              are 'savings' and 'cd'
        # Return the validated user input as a dictionary
            - create_savings_account and create_cd_account
              both require balance, interest_rate, and months as arguments, so
              return a dictionary of validated user input using the keys
              'balance', 'interest_rate', and 'months'
    '''
    # Prompt the user to set the balance, interest rate, and months for the account.
    # Let's test all of these user inputs one at a time so that the user can
    # correct any mistakes as they go along
    balance_validated = False
    while not balance_validated:
        balance = input(f"Enter the {account_type} account starting balance:  ")
        balance_validated = validate_type(balance, 'float')

    interest_validated = False
    while not interest_validated:
        interest = input(f"Enter the interest rate as a decimal for the"
                         f" {account_type} account:  ")
        interest_validated = validate_type(interest, 'float')

    months_validated = False
    while not months_validated:
        months = input(f"Enter the number of months for the {account_type} account:  ")
        months_validated = validate_type(months, 'int')
    # Now we have all inputs validated, so let's return our clean results in a 
    # dictionary.
    return {'balance': balance_validated,
            'interest_rate': interest_validated,
            'months': months_validated}


# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    valid_savings_input = collect_user_input('savings')

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, savings_interest_earned = create_savings_account(**valid_savings_input)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"This account earned $ {savings_interest_earned:,.2f} in interest"
          f" over the last {valid_savings_input['months']} months.\n"
          f"The updated balance is $ {updated_savings_balance:,.2f}.")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    valid_cd_input = collect_user_input('cd')

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_interest_earned = create_cd_account(**valid_cd_input)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"This account earned $ {cd_interest_earned:,.2f} in interest over the"
          f" last {valid_cd_input['months']} months.\n"
          f"The updated balance is $ {updated_cd_balance:,.2f}.")

if __name__ == "__main__":
    main()
