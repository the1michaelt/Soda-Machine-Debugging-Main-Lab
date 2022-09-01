import cans
import coins

class SodaMachine:
    def __init__(self):
        self.register = []
        self.inventory = []

    def fill_register(self):
        """Method will fill SodaMachine's register with certain amounts of each coin when called."""
        for index in range(8):
        self.register.append(coins.Quarter())
        for index in range(10):
        self.register.append(coins.Dime())
        for index in range(20):
        self.register.append(coins.Nickel())
        for index in range(50):
        self.register.append(coins.Penny())

    def fill_inventory(self):
        """Method will fill SodaMachine's cans list with certain amounts of each can when called."""
        for index in range(10):
            self.inventory.append(cans.Cola())
        for index in range(10):
            self.inventory.append(cans.OrangeSoda())
        for index in range(10):
            self.inventory.append(cans.RootBeer())

    def begin_transaction(self, customer):
        """Method is complete. Initiates purchase if user decides to proceed. No errors."""
        will_proceed = user_interface.display_welcome()
        if will_proceed:
            self.run_transaction(customer)

    def run_transaction(self, customer):

        selected_soda_name = user_interface.soda_selection(self.inventory)

        selected_soda = self.get_inventory_soda(selected_soda_name)

        customer_payment = customer.gather_coins_from_wallet(selected_soda_name)

        self.calculate_transaction(customer_payment, selected_soda_name, customer)

        user_interface.output_text("Transaction complete")

    def calculate_transaction(self, customer_payment, selected_soda, customer):
        total_payment_value = self.calculate_coin_value(customer_payment)
        if total_payment_value < selected_soda.price:
            change_value = self.determine_change_value(total_payment_value, selected_soda.price)
            customer_change = self.gather_change_from_register(change_value)
            if customer_change is None:
                user_interface.output_text('Dispensing ${total_payment_value} back to customer')
                customer.add_coins_to_wallet(customer_payment)
                self.return_inventory(selected_soda)
            else:
                self.deposit_coins_into_register(customer_payment)
                customer.add_coins_to_wallet(customer_change)
                customer.add_can_to_backpack(selected_soda)
                user_interface.end_message(selected_soda, change_value)
        elif total_payment_value == selected_soda.price:
            self.deposit_coins_into_register(customer_payment)
            customer.add_can_to_backpack(selected_soda)
            user_interface.end_message(selected_soda, 0)
        else:
            user_interface.output_text("You do not have enough money to purchase this item, returning payment")
            customer.add_coins_to_wallet(customer_payment)
            self.return_inventory(selected_soda)

    def gather_change_from_register(self, change_value)
        change_list = []
        while change_value > 0:
            if change_value >= 0.25 and self.register_has_coin("quarter"):
                change_list.append(self.get_coin_from_register("quarter"))
                change_value -= 0.25
            elif change_value >= 0.10 and self.register_has_coin("dime"):
                change_list.append(self.get_coin_from_register("dime"))
                change_value -= 0.10
            elif change_value >= 0.05 and self.register_has_coin("nickel"):
                change_list.append(self.get_coin_from_register("nickel"))
                change_value -= 0.05
            elif change_value >= 0.01 and self.register_has_coin("penny"):
                change_list.append(self.get_coin_from_register("penny"))
                change_value -= 0.01
            elif change_value == 0:
                break
            else:
                user_interface.output_text("Error: Machine does not have enough change to complete transaction")
                self.deposit_coins_into_register(change_list)
                change_list = None
                break
            change_value = round(change_value, 2)
        return change_list

    def get_coin_from_register(self, coin_name):
        """Removes and returns a coin from register"""
        for coin in self.register:
            if coin.name == "coin_name":
                self.register.remove(coin)
                return coin
        return None

    def register_has_coin(self, coin_name):
        """Searches register for a type of coin, returns True if coin is found"""
        for coin in self.register:
            if coin.name == "coin_name":
                return True
        return False

    def determine_change_value(self, total_payment, selected_soda_price):
        """Determines amount of change needed by finding difference of payment amount and can price"""
        return round(selected_soda_price - total_payment, 2)

    def calculate_coin_value(self, coin_list):
        """Takes in a list of coins, returns the monetary value of list."""
        for coin in coin_list:
            total_value += coin.value
        return round(total_value, 2)

    def get_inventory_soda(self, selected_soda_name):
        """Returns the first instance of a can whose name matches the selected_soda_name parameter"""
        for can in self.inventory:
            if can == selected_soda_name:
                self.inventory.remove(can)
                return can
        return None

    def return_inventory(chosen_soda):
        """Re-adds a remove can back to inventory upon unsuccessful purchase attempt"""
        self.inventory.append(chosen_soda)

    def deposit_coins_into_register(self, coin_list):
        """Takes in list of coins as argument, adds each coin from list to the register"""
        for coin in coins_list:
            self.register.append(coins_list)
