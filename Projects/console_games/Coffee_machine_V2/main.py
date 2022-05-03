from Menu import Menu
from Coffee_Maker import CoffeeMaker
from Money_Machine import MoneyMachine
from logo import logo


def play_game():
    print(logo)
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money = MoneyMachine()

    while True:
        choice = input(f"​What would you like? {menu.get_items()}: ")
        drink = menu.find_drink(choice)
        if choice == "report":
            coffee_maker.report()
        elif drink != None:
            if coffee_maker.is_resource_sufficient(drink):
                if money.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
        else:
            return


play_game()
while str(input("Do you want to refill the Tank? 'Yes' or 'No'")) == "Yes":
    play_game()
