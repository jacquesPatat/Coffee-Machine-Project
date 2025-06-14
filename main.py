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

profit = 0

def report():
    """Prints the current resource levels and profit."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources.get('milk', 0)}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit:.2f}")

def is_resource_sufficient(ingredients):
    """Checks if there are enough resources to make the drink."""
    for item in ingredients:
        if ingredients[item] > resources.get(item, 0):
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def make_coffee(drink_name, ingredients):
    """Deducts ingredients and serves the drink."""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink_name}. Enjoy! ☕")

# Main loop
is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        is_on = False
        print("Turning off the coffee machine. Goodbye!")
    elif choice == "report":
        report()
    elif choice in MENU:
        drink = MENU[choice]
        cost = drink["cost"]
        if is_resource_sufficient(drink["ingredients"]):
            print(f"The price is ${cost:.2f}.")
            proceed = input("Would you like to proceed with payment? (yes/no): ").lower()
            if proceed == "yes":
                print(f"Processing payment of ${cost:.2f}... (payment spoofed)")
                profit += cost
                make_coffee(choice, drink["ingredients"])
            else:
                print("Transaction cancelled.")
    else:
        print("Invalid input. Please select espresso, latte, or cappuccino.")

#when prompted for espresso/latte/cappuccino - type report to see how much ingredients is left.
#when prompted for espresso/latte/cappuccino - type off to exit application
