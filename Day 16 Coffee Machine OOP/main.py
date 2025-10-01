from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine = CoffeeMaker()
menu = Menu()
moneyMachine = MoneyMachine()

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino/): ")

    if choice in menu.get_items().split("/")[:-1]:
        drink = menu.find_drink(choice)
        # Check if resources are sufficient to make the drink:
        if machine.is_resource_sufficient(drink):
            # Make payment
            if moneyMachine.make_payment(drink.cost):
                machine.make_coffee(drink)
    elif choice == 'off':
        print("Coffee machine turning off.")
        is_on = False
    elif choice == 'report':
        machine.report()
    else:
        print("Invalid input. Please try again.")
