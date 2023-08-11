import os
from art_day8 import logo
print(logo)
end=False
Persons=[]
print("Welcome to the secret auction program.")
while end== False:

    

    name=input("what is your name?: ")
    bid=int(input("what's your bid?: "))
    pers={}
    pers["name"]= name
    pers["bid"]= bid
    Persons.append(pers)
    print(Persons)
   
    conti=input("Do you want to add another person yes or no: ")
    if conti=="no":
        end=True
        os.system('cls')
    os.system('cls')
highest_name=""
highest_Bid=0
highest_num=0
for i in range(0,len(Persons)):

    
    if Persons[i]["bid"]>highest_num:
        highest_name=Persons[i]["name"]
        highest_Bid= Persons[i]["bid"]
        highest_index=i

print(f"the Winner is {highest_name} ")

print(f"with a bid of {highest_Bid}")

    

