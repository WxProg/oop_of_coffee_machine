from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def blue_cups():
    # List of all the objects used in the program
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    menu = Menu()

    brewing = True
    while brewing:
        print("\nIf your an employee or maintenance worker enter 'off' or 'report' to turn of machine or get report.")
        decision = input(f"What would you like to drink? ({menu.get_items()}): ")

        if decision == 'off':
            print("Machine is off!")
            brewing = False
        elif decision == 'report':
            coffee_maker.report()
            money_machine.report()
        else:
            coffee_drink = menu.find_drink(decision)
            if coffee_maker.is_resource_sufficient(coffee_drink) and money_machine.make_payment(coffee_drink.cost):
                coffee_maker.make_coffee(coffee_drink)
                print(f"The cost of your {coffee_drink.name}, was ${coffee_drink.cost} and "
                      f"its ingredients{coffee_drink.ingredients}")


blue_cups()
