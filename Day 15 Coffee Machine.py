coffees = [
    {'name': 'espresso', 'water': 50, 'milk': 0, 'coffee': 18, 'cost': 1.5},
    {'name': 'latte', 'water': 200, 'milk': 150, 'coffee': 24, 'cost': 2.5},
    {'name': 'cappuccino', 'water': 250, 'milk': 100, 'coffee': 24, 'cost': 3.0}
]

resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
    'money': 0
}

coins = {
    'quarters': 0.25,
    'dimes': 0.10,
    'nickels': 0.05,
    'pennies': 0.01
}

# Program Requirements
# 1. Print report of all resources.
# 2. Check resources sufficient?
# 3. Process coins.
# 4. Check transaction successful?
# 5. Make Coffee.

def printReport():
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}g\nMoney: ${resources['water']}")

def checkResources(coffee):
    if resources['water'] < coffee['water']:
        print("Not enough water.")
        return False
    elif resources['milk'] < coffee['milk']:
        print("Not enough milk.")
        return False
    elif resources['coffee'] < coffee['coffee']:
        print("Not enough coffee.")
        return False
    else:
        return True

def processCoins():
    print("Please insert coins.")
    quarters = int(input("How many Quarters: "))
    dimes = int(input("How many Dimes: "))
    nickels = int(input("How many Nickels: "))
    pennies = int(input("How many Pennies: "))
    total = (quarters * coins['quarters']) + (dimes * coins['dimes']) + (nickels * coins['nickels']) + (pennies * coins['pennies']) 
    return total

def checkTransaction(money, coffee):
    if money < coffee['cost']:
        print("Sorry that's not enough money. Money refunded.")
    else:
        change = round((money - coffee['cost']), 2)
        if change != 0:
            print(f"Here is ${change} in change.")
        resources['money'] += money

def makeCoffee(coffee):
    for resource in resources:
        if resource != 'money':
            resources[resource] -= coffee[resource]
    print(f"Enjoy your {coffee['name']}.")
        


while True:
    choice = input("What type of coffee do you want? ").lower()
    if choice in ['espresso','latte','cappuccino']:
        for coffee in coffees:
            if coffee['name'] == choice:
                if checkResources(coffee):
                    insertedMoney = processCoins()
                    checkTransaction(insertedMoney, coffee)
                    makeCoffee(coffee)
                    
    elif choice == 'report':
        printReport()
    else:
        print("Invalid option. Please try again.")