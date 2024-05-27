# Menu dict
menu = {
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

# Resource dict
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

MONEY = 0


def check_ingredients(choice,resources=resources,menu=menu):
    for ingredient, required_value in  menu[choice]['ingredients'].items():
        for resource, disposable_value in resources.items():
            if required_value > disposable_value:
                return False
            else:
                return True


# Assign variables:
available_water = resources['water']
available_milk = resources['milk']
available_coffee = resources['coffee']
# Secret way of turning of the machine and also for generating report of the machine
coffee_machine_working = True
#eoed
while coffee_machine_working:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == 'off':
        coffee_machine_working = False
    elif choice == 'report':
        print(f'Water: {available_water}ml\nMilk: {available_milk}ml\nCoffee: {available_coffee}g\nMoney: ${MONEY}')
    elif choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
        coffeeAvailability = check_ingredients(choice)

        cost_of_choice = menu[choice]['cost']
        required_water = menu[choice]['ingredients']['water']
        if choice != 'espresso':
            required_milk = menu[choice]['ingredients']['milk']
        else:
            pass
        required_coffee = menu[choice]['ingredients']['coffee']

        if coffeeAvailability:
            money_request = float(input(f"Please insert the required funds ({cost_of_choice}$): "))
            if money_request < cost_of_choice:
                print(f"Not enough money! Money refunded (${money_request}).")
            elif money_request == cost_of_choice:
                MONEY += cost_of_choice
            elif money_request > cost_of_choice:
                print(f"Here is ${round(money_request - cost_of_choice, 2)} in change.")
                MONEY += cost_of_choice
        else:
            print("Sorry there is not enough resources to make this coffee.")
            coffee_machine_working = False
        if choice != 'espresso':
            available_milk -= required_milk
        else:
            pass
        available_water -= required_water
        available_coffee -= required_coffee
        print(f"Here is your {choice}. Enjoy!")
    else:
        print(f"Wrong choice. There is no {choice} on the menu. Please try again.")


#
