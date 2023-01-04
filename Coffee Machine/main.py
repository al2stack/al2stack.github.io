from data import MENU
from data import resources
#TODO function to check for enough resources
def check_resources(type):
    ingredient = MENU[type]["ingredients"]

    for item in ingredient:
        if resources[item] < ingredient[item]:
            print(f"I don't have enough {item}")
            return False

    return True
def add(a,b,c,d):
    return a+b+c+d
def process_transaction(type,money):
    coffee_cost=MENU[type]["cost"]
    if coffee_cost>money:
        print("Sorry that's not enough money. You have been refunded")
    elif coffee_cost<=money:
        change=round(money-coffee_cost,2)
        global money_in_machine
        money_in_machine+=coffee_cost
        print(f"Thank you, your change is: ${change}")
        return True

def make_coffee(type):
    ingredient=MENU[type]["ingredients"]
    for item in ingredient:
        resources[item]=resources[item]-ingredient[item]


money_in_machine=0.00

quarters=0.25
dimes=0.1
nickel=0.05
pennies=0.01
is_on=True

while is_on:
    choice = input("What do you want?(espresso/latte/cappuccino): ").lower()
    if choice == "report":
        for item in resources:
            print(item + ": " + str(resources[item]))
        print("Money: $"+str(money_in_machine))
    elif choice=="off":
        print("Coffee machine is shutting down now!")
        is_on=False
    else:
        enough=check_resources(choice)
        if enough:
            quarters *= int(input("How many quarters? "))
            dimes *= int(input("How many dimes? "))
            nickel *= int(input("How many nickels? "))
            pennies *= int(input("How many pennies? "))
            total = add(quarters, dimes, nickel, pennies)
            valid=process_transaction(choice, total)
            if valid:
                make_coffee(choice)
                print(f"Here is your {choice}, enjoy!")


