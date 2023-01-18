from customer import Customer
from soda_machine import SodaMachine 
import user_interface

class Simulation:
    def __init__(self):
        pass

    def run_simulation(self):
        """The central method called in main.py."""
        customer = Customer()
        soda_machine = SodaMachine()
        will_proceed = True

        while will_proceed:
            user_option = user_interface.simulation_main_menu()
            if user_option == 0:
                soda_machine.begin_transaction(customer)
            elif user_option == 1:
                customer.check_coins_in_wallet()
                # customer.check_coins_in_wallet(self)
            elif user_option == 2:
                customer.check_backpack()
                # customer.check_backpack(purchased_cans)
            else:
                will_proceed = False
