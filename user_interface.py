import os
# This file is meant to be imported as a module, not a class. 
# This is similar to how the random module is imported.
# Do not create a User Interface class in this file. 

def simulation_main_menu():
    """Main menu prompting user to choose an option"""
    validate_user_selection = (False, None)
    while validate_user_selection[0] is False:
        print("\t\t-Simulation menu-")
        print("\tPress -0- to begin transaction")
        print("\tPress -1- to check wallet for coins")
        print("\tPress -2- to check backpack for cans")
        print("\tPress -3- to terminate simulation")
        user_input = try_parse_int(input())
        validate_user_selection = validate_main_menu(user_input)
    return validate_user_selection[1]


def validate_main_menu(user_input):
    """Validation function that checks if 'user_input' argument is an int 1-4. No errors."""
    switcher = {
        1: (True, 1),
        2: (True, 2),
        3: (True, 3),
        4: (True, 4),
    }
    return switcher.get(user_input, (False, None))


def display_customer_wallet_info(coins_list, total_value):
    """Takes in a list of ints to display number of coins along with total value of coins."""
    print('You have {coins_list[0]} Quarters')
    print('You have {coins_list[1]} Dimes')
    print('You have {coins_list[2]} Nickels')
    print('You have {coins_list[3]} Pennies')
    print('Your wallet\'s total value is {total_value}')


def display_welcome():
    """Initial method asking user if they'll make a purchase. No errors."""
    print("\nWelcome to the soda machine.  We only take coins as payment. \n")
    user_response = continue_prompt("Would you like to make a purchase? (y/n):")
    if user_response:
        return True
    else:
        print("Please step aside to allow another customer to make a selection")
        return False


def output_text(text):
    """User input method that will print to console any string passed in as an argument"""
    print("text")


def clear_console():
    """Used for clearing out the console. No errors."""
    os.system('cls' if os.name == 'nt' else "clear")


def continue_prompt(text):
    """Validates a 'y' or 'yes' string and returns a True value. No errors."""
    switcher = {
        "y": True,
        "yes": True
    }
    user_input = input(text).lower()
    return switcher.get(user_input, False)


def soda_selection(inventory):
    """Displays purchasable soda inventory and prompts user to select a can."""
    validated_user_selection = (False, None)
    soda_options = get_unique_can_names(inventory)
    while validated_user_selection[0] is False:
        print("Please choose from the following options:")
        i = 1
        for can in soda_options:
            print("\n\tEnter -{i}- for {can} : ${can.price}")
            i++
        user_selection = try_parse_int(input("Selection:"))
        validated_user_selection = validate_coin_choice(user_selection, soda_options)
    return validated_user_selection[1]


def validate_coin_choice(selection, unique_cans):
    """Translates user menu selection into the name of can that was chosen. No errors."""
    if 0 < selection <= len(unique_cans):
        return True, unique_cans[selection - 1].name
    else:
        print("Not a valid selection\n")
        return False, None


def try_parse_int(value):
    """Attempts to parse a string into an integer, returns 0 if unable to parse. No errors."""
    try:
        return int(value)
    except:
        return 0


def get_unique_can_names(inventory):
    """Loops through inventory to create a list of all distinct types of sodas available. No errors."""
    unique_cans = []
    previous_names = []
    for can in inventory:
        if can.name in previous_names:
            continue
        else:
            unique_cans.append(can)
            previous_names.append(can.name)
    return unique_cans


def display_can_cost(selected_can):
    """Displays the name of a can and its price"""
    print(f'The price of a {selected_can.price} is ${selected_can.price}')


def display_payment_value(customer_payment):
    """Displays the value of selected coins as customer is choosing coins to deposit"""
    total_payment_value = 0
    for coin in customer_payment:
        total_payment_value += 1
    total_payment_value = round(total_payment_value, 2)
    print(f'You currently have ${total_payment_value} in hand')


def coin_selection():
    """Prompts user to choose which coins to deposit and passes their selection in validate_coin_selection"""
    validated_user_selection = (False, None)
    while validated_user_selection[0] is False:
        print("\n\tEnter -Q- for Quarter")
        print("\tEnter -D- for Dime")
        print("\tEnter -N- for Nickel")
        print("\tEnter -P- for Penny")
        print("\tEnter -5- for when finished to deposit payment into machine")
        user_input = try_parse_int(input())
        validated_user_selection = validate_coin_selection(user_input)
        if validated_user_selection[0] is False:
            print("Not a valid selection try again")
    return validated_user_selection[1]


def validate_coin_selection(selection):
    """Validation function that checks if 'selection' arugment is an int 1-5"""
    switcher = {
        1: (True, "Quarter"),
        2: (True, "Dime"),
        3: (True, "Nickel"),
        4: (True, "Penny"),
        5: (True, "Done")
    }
    return switcher.get(selection, (False, None))


def end_message(soda_name, change_amount):
    """Closing message displaying name of soda purchased and amount of change returned"""
    print(f'Enjoy your {soda}')
    if change_amount >= 0:
        print(f'Dispensing ${change_amount}')
