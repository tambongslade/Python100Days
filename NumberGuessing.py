import random

NUM=random.randint(0,100)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
choice=input("Choose a difficulty. Type 'easy or 'hard': ")
def num(n):
    if choice=="easy":
        return 10
    elif choice=="hard":
        return 5
lives=num(choice)
win=False
while win==False:
    
    if lives==0:
        print("you failed")
        win=True
    print(f"you have {lives} attempts remaining to guess the number.")
    guess=int(input("make a Guess: "))
    if guess==NUM:
        print(f"You guessed the number it's {NUM}")
        win=True
    elif guess>NUM:
        print("your number is too high")
        lives-=1
    elif guess<NUM:
        print("your number is too low")
        lives-=1
