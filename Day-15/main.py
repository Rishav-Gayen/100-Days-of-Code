from data import MENU, resources
from art import logo

machine_is_on = True

def print_report():
    """Prints the current resource levels and total money in the coffee machine."""
    
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${resources["money"]}")
    

def check_resources_sufficient(drink_name):
    """Checks if there are enough resources to make the selected drink."""

    drink = MENU[drink_name]
    ingredients = drink["ingredients"]

    for ingredient in ingredients:
        if ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry there's not enough {ingredient}")
            return False
    
    return True

def process_coins():
    """Prompts the user to insert coins and calculates the total monetary value."""

    quarters = int(input("How many quarters do you want to insert?: ")) * 0.25
    dimes = int(input("How many dimes you want to insert?: ")) * 0.10
    nickels = int(input("How many nickels you want to insert?: ")) * 0.05
    pennies = int(input("How many pennies you want to insert: ")) * 0.01

    total_amount = quarters + dimes + nickels + pennies

    return total_amount

def check_transaction_successful(amount, drink_name):
    """Checks if the inserted money is enough to purchase the selected drink."""

    cost = MENU[drink_name]["cost"]
    if amount >= cost:
        resources["money"] += cost
        change = amount - MENU[drink_name]["cost"]
        if change > 0:
            print(f"Here's ${round(change, 2)} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money Refunded.")
        return False
    

def make_coffee(drink_name):
    """Deducts the required ingredients from resources and serves the coffee."""

    ingredients = MENU[drink_name]["ingredients"]
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]
    
    print(f"Here's your {drink_name}!☕ Enjoy!")


print(logo)

while machine_is_on:
    correct_input = False
    correct_inputs = ["latte", "espresso", "cappuccino", "report", "off"]
    drink_name = ""

    while not correct_input:
        drink_name = input("What would you like (latte/espresso/cappuccino)?: ")
        drink_name = drink_name.lower()

        if drink_name in correct_inputs:
            if drink_name == 'report':
                print_report()
            elif drink_name == 'off':
                machine_is_on = False
            else:
                if check_resources_sufficient(drink_name):
                    amount = process_coins()
                    if check_transaction_successful(amount, drink_name):
                        make_coffee(drink_name)
            correct_input = True





