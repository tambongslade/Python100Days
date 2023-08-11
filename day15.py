#day 15
from resourcescoffe import MENU
machine={"Water":300,"milk":200,"Coffee":100,"money":0}



#print Report
def report():
    print(f"Water: {machine['Water']}\nMilk: {machine['milk']}\nCoffee: {machine['Coffee']}\nMoney: {machine['money']}")
#check resources sufficent
def req(n):
    if n=="espresso" and machine["Water"]>=MENU[f"{n}"]["ingredients"]["water"] and  machine["Coffee"]>=MENU[f"{n}"]["ingredients"]["coffee"]:
        return True
    elif machine["Water"]>=MENU[f"{n}"]["ingredients"]["water"] and machine["milk"]>=MENU[f"{n}"]["ingredients"]["milk"]and machine["Coffee"]>=MENU[f"{n}"]["ingredients"]["coffee"]:
        return True
    else:
        return False
def processcoin():
    print("Please insert a coins.")
    quater=int(input("How Many Quaters?: "))
    dimes=int(input("How Many Dimes?: "))
    nickles=int(input("How Many Nickles?: "))
    pennies=int(input("How Many Pennies?: "))
    return (quater*0.25)+(dimes*0.10)+(nickles*0.5)+(pennies*0.1)
def checkTransaction(u,m):
    if m>MENU[f"{u}"]["cost"]:
        print(f"Here is your {userChoice} 😊 enjoy")
        return m-MENU[f"{u}"]["cost"]
    else:
        print("your money is not sufficient, Money refunded")
def makeCoffee():
    if userChoice=="espresso":
        machine["Coffee"]=machine["Coffee"]-MENU[userChoice]["ingredients"]["coffee"]
        machine["Water"]=machine["Water"]-MENU[userChoice]["ingredients"]["water"]
        machine["money"]=machine["money"]+MENU[userChoice]["cost"]
    else:
          machine["Coffee"]=machine["Coffee"]-MENU[userChoice]["ingredients"]["coffee"]
          machine["Water"]=machine["Water"]-MENU[userChoice]["ingredients"]["water"]
          machine["milk"]=machine["milk"]-MENU[userChoice]["ingredients"]["milk"]
          machine["money"]=machine["money"]+MENU[userChoice]["cost"]


while True:
        
    userChoice=input("what would you like? (espresso/latte/cappuccino): ")
    if userChoice=="report":
        report()
    elif userChoice=="espresso":
        if req(userChoice)==True:

            usermoney=processcoin()
            print(f"your change is {checkTransaction(userChoice,usermoney)}")
            makeCoffee()
        else:
            print("insufficient ingredients")
    elif userChoice=="latte":
         if req(userChoice)==True:

            usermoney=processcoin()
            print(f"your change is {checkTransaction(userChoice,usermoney)}")
            makeCoffee()
         else:
            print("insufficient ingredients")
    elif userChoice=="cappuccino":
             if req(userChoice)==True:

                usermoney=processcoin()
                print(f"your change is {checkTransaction(userChoice,usermoney)}")
                makeCoffee()
             else:
                print("insufficient ingredients")



#process coin

#check transaction 

#make coffee