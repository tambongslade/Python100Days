# import random
# ran= random.randint(0,1)
# print(ran)
# if(ran==1):
#     print("head")
# else:
#     print("tail")
# import random
# name_String= input("Give me everbody's names, seperated by a comma. ")
# names=name_String.split(", ")
# num=len(names)
# print(num)
# ran= random.randint(0,num-1)
# print(ran)
# print(f"{names[ran]} is going to pay")
# row1= ['⬜️', '⬜️', '⬜️']
# row2= ['⬜️', '⬜️', '⬜️']
# row3= ['⬜️', '⬜️', '⬜️']
# map=[row1,row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position= input(" where do you want to put the treasure? ")
# index1=int(position[0])
# index2=int(position[1])
# map[index1-1][index2-1]='X'
# print(f"{row1}\n{row2}\n{row3}")
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
al=[rock,paper,scissors]

choice=input("what do you choose? Type 0 for Rock,1 for Paper or 2 for Scissors")
choice=int(choice)
ran= random.randint(0,len(al)-1)
print(choice)
print(ran)
print(f"{al[choice]}\n computer choice:\n {al[ran]}")
if choice==0 and ran==2 or choice==1 and ran==0 or choice==2 and ran==1:
    print("you Won")
elif choice==ran:
    print("Draw")
else:
    print("You Lose")
