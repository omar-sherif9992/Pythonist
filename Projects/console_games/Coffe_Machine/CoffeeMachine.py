from Menu import MENU
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit=0

def process_coin():
    money=float(input("How many Quarters"))*0.25
    money += float(input("How many Dimes")) * 0.1
    money += float(input("How many Nickles")) * 0.05
    money += float(input("How many Pennies")) * 0.01
    return money

def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    global profit
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
def check_resources(choosen):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for ingredient in choosen["ingredients"]:
         print(ingredient)
         if resources[f"{ingredient}"]<choosen["ingredients"][ingredient]:
             print(f"​Sorry there is not enough {ingredient}.")
             return False
    return True

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


def play_game():
    profit=0
    while True:
        choice = input("​What would you like? (espresso/latte/cappuccino): ")
        if choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${profit}")


        elif check_resources(MENU[choice]):
                money=process_coin()
                if is_transaction_successful(money, MENU[choice]["cost"]):
                    make_coffee(choice, MENU[choice]["ingredients"])
        else:
            return




play_game()
while str(input("Do you want to refill the Tank? 'Yes' or 'No'")) =="Yes":
    play_game()


