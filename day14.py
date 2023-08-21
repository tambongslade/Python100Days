import random
from higher_logo import logo,vs
from higher_data import data
import os
score=0
lies=False
print(logo)
cus1= data[random.randint(0,len(data)-1)]
cus2= data[random.randint(0,len(data)-1)]
def generateCus():
    global cus1,cus2
    cus1= data[random.randint(0,len(data)-1)]
    cus2= data[random.randint(0,len(data)-1)]
def NextGame():
    print(logo)
    print(f"you're right, Current Score: {score}")
    print(f'compare A: {cus1["name"]}, a {cus1["description"]}, from {cus1["country"]}')
    print(vs)
    print(f'agaisnt B: {cus2["name"]}, a {cus2["description"]}, from {cus2["country"]}')
    choice=input("who has the more followers? Type 'A' or 'B':  ")
    return choice
def failed():
    os.system('cls')
    print(logo)
    print(f"Sorry your wrong, Final score {score}")
def checkchoice(n):
    if n=="A" and cus1["follower_count"]>cus2["follower_count"]:
        return False
    elif n=="B" and cus2["follower_count"]>cus1["follower_count"]:
        return False
    else:
        return True   

print(f'compare A: {cus1["name"]}, a {cus1["description"]}, from {cus1["country"]}')
print(vs)
print(f'agaisnt B: {cus2["name"]}, a {cus2["description"]}, from {cus2["country"]}')
choice=input("who has the more followers? Type 'A' or 'B':  ")
while checkchoice(choice)==False:
        score+=1
        os.system('cls')
        
        generateCus()
        NextGame()

    
failed()
        


 
