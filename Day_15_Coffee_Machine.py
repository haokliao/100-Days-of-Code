#three hot flavors
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

# 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino): ”
    # a. Check the user’s input to decide what to do next.
    # b. The prompt should show every time action has completed, e.g. once the drink is
    # dispensed. The prompt should show again to serve the next customer.
# 2. Turn off the Coffee Machine by entering “off” to the prompt.
# a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
# the machine. Your code should end execution when this happens.
# 3. Print report.
# a. When the user enters “report” to the prompt, a report should be generated that shows
# the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# 4. Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “Sorry there is not enough water.”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.
machine_on = True

def sufficient(order):
    for item in order:
        if order[item] >= resources[item]:
            print(f'Sorry, there is not enough {item}.')
            return False
    return True

def coins():
    """process coins"""
    print ('Please insert coins')
    total = int(input('How many quarters: ')) * 0.25
    total += int(input('How many dimes: ')) * 0.1
    total += int(input('How many nickels: ')) * 0.05
    total += int(input('How many pennies: ')) * 0.01
    return total

def works(money_received,drink_price):
    """ T or F when money is accepted"""
    if money_received>= drink_price:
        change = round(money_received - drink_price,2)
        print(f'Here\'s your change {change}')
        global profit 
        profit += money_received
        return True
    else:
        return False
        print('Give more moneyz')

def coffee(drink_name,ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]



while machine_on:
    choice = input(f'What would you like? (Espresso/Latte/Cappuccino?) : \n')
    if choice == 'off':
        machine_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk:  {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else: 
        drink = MENU[choice]
        if sufficient(drink['ingredients']):
            payment = coins()
            works(payment,drink['cost'])
            coffee(coffee,drink['ingredients'])


# 5. Process coins.
    # a. If there are sufficient resources to make the drink selected, then the program should
    # prompt the user to insert coins.
    # b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    # c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
    # pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
# 6. Check transaction successful?
    # a. Check that the user has inserted enough money to purchase the drink they selected.
        # E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
        # program should say “Sorry that's not enough money. Money refunded.”.
    # b. But if the user has inserted enough money, then the cost of the drink gets added to the
        # machine as the profit and this will be reflected the next time “report” is triggered. E.g.
        # Water: 100ml
        # Milk: 50ml
        # Coffee: 76g
        # Money: $2.5
    # c. If the user has inserted too much money, the machine should offer change.
        # E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
        # places.
# 7. Make Coffee.
    # a. If the transaction is successful and there are enough resources to make the drink the
    # user selected, then the ingredients to make the drink should be deducted from the
    # coffee machine resources.
        # E.g. report before purchasing latte:
        # Water: 300ml
        # Milk: 200ml
        # Coffee: 100g
        # Money: $0
        # Report after purchasing latte:
        # Water: 100ml
        # Milk: 50ml
        # Coffee: 76g
        # Money: $2.5
    # b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
    # latte was their choice of drink.
