from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
men=Menu()
items=MenuItem
cof=CoffeeMaker()
mone=MoneyMachine()
while True:
    choice=input(f"Choose your drink {men.get_items()}?")
    if choice=="report":
        cof.report()
        mone.report()
    elif men.find_drink(choice)!= None:
        drink=men.find_drink(choice)
        if cof.is_resource_sufficient(drink)==True:
                mone.make_payment(drink.cost)
                cof.make_coffee(drink)



    

