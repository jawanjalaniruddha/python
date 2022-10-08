# ☕
import sys

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO: Create a function to take order :- take_order()
# TODO: Create a function to check if resources are sufficient  :- check_resources()
# TODO: Make coffee and give it to user if resources are sufficient. Prompt again for order
# TODO: Collect money. Return change if there's any
# TODO: Create a function to print report with available resources
# TODO: Create condition to switch off machine

profit = 0


def check_resources(coffee_type):
    for each_ingredients in MENU[coffee_type]["ingredients"]:
        if MENU[coffee_type]["ingredients"][each_ingredients] > resources[each_ingredients]:
            print(f"Sorry there is not enough {each_ingredients}")
            return False
        else:
            return True


def process_coins(coffee_type):
    global profit
    quarters = int(input("please insert quarters: "))
    dimes = int(input("please insert dimes: "))
    nickles = int(input("please insert nickles: "))
    pennies = int(input("please insert pennies: "))
    amount = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    if amount >= MENU[order]["cost"]:
        amount = round(amount - MENU[order]["cost"], 2)
        profit = profit + MENU[order]["cost"]
        print(f"Here is ${amount} dollars in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def report():
    global profit
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money Collected: ${profit}")


machine_on = True
while machine_on:
    order = input(f"What would you like? (espresso/latte/cappuccino/): ")
    if order == "report":
        report()
    elif order == "off":
        print("Shutting down...")
        machine_on = False
    elif check_resources(order):
        for each_ingredients in MENU[order]["ingredients"]:
            resources[each_ingredients] = resources[each_ingredients] - MENU[order]["ingredients"][each_ingredients]
        if process_coins(order):
            print(f"Here is your {order}☕. Enjoy!")










