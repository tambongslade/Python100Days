# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run i
student_scores=[78,65,89,86,55,91,64,89]
highest_score= 0
for score in student_scores:
    print(highest_score)
    if score> highest_score:
        highest_score=score
print(f"the highest number is {highest_score}")
total=0
for i in range(1,101,2):
    total=i+total
print(total)

for i in range(1,101):
    if(i%3==0 and i%5==0):
        print("fizzbuz")
    elif(i%5==0):
        print("buzz")
    elif(i%3==0):
        print("fizz")
    else:
        print(i)
# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
password = ""
nr_letters = int(input("How many letters would you like in your password?\n"))

nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password = []
# not randomized
for i in range(0, nr_letters):
    password.append(random.randint(0, len(letters) - 1))
print(password)
for i in range(0, nr_symbols):
    password.append(random.randint(0, len(symbols) - 1))

print(password)
for i in range(0, nr_numbers):
    password.append(random.randint(0, len(numbers) - 1))

print(type(password))
passx = ""
for i in password:
    passx[i] = password[i]

random.shuffle(passx)
password = ""
for i in passx:
    password = password + passx[i]
print(f"this is the randomise array {password}")