#if/ else statements
print("Welcome to the rollercoaster")
height= int(input("what is your height in cm?"))
if height>120:
    print("you can ride the rollercoaster")
else:
    print("Sorry you can't ride you are too short")
    # odd or even numner
    if number % 2 == 0:
        print("it is an even number")
    else:
        print("it is an odd number")
        print("Welcome to the rollercoaster")
        height = int(input("what is your height in cm?"))
        if height > 120:
            age = int(input("enter your age:"))
            if age < 12:
                print("you will pay $5")
            elif age > 12 and age < 18:
                print("you will pay $7")
            elif age > 18:
                print("you will pay $12")

        else:
            print("Sorry you can't ride you are too short")

    #bmi calculator
    height = float(input("Enter your height in m: "))
    weight = float(input("Enter your weight in kg: "))
    bmi = round(weight / height ** 2)
    print(f"your bmi score is {bmi}")
    if bmi < 18.5:
        print("you are underweight")
    elif bmi < 25:
        print(" you are normal weight")
    elif bmi < 30:
        print(" you are overweight")
    elif bmi < 35:
        print(" you are obese")
    else:
        print("you are clinically obese")
    #leap year
    year = int(input("Which year do you want to check?"))
    if year % 4 == 0:
        if year % 100 != 0:
            if year % 400 != 0:
                print(f"{year}is a leap year")
    else:
        print(f"{year} is not a leap year")
        # Online Python compiler (interpreter) to run Python online.
        # Write Python 3 code in this online editor and run it.
        print("welcome to python Pizza deliveries ")
        size = input("what size pizza do you want? S,M or L? ")
        add_pepperoni = input("Do you want Pepperoni? Y or N? ")
        extra_chesse = input("Do you want extra chees?, Y or N? ")
        price = 0
        if (size == 'S'):
            price += 15
            if (add_pepperoni == 'Y'):
                price += 2
        elif (size == 'M'):
            price += 20
            if (add_pepperoni == 'Y'):
                price += 3
        elif (size == 'L'):
            price += 25
            if (add_pepperoni == 'Y'):
                price += 3
        if (extra_chesse == 'Y'):
            price += 1
        print(f"The final bill is: ${price}")
        print("Welcome to the love Calculator!")
        name1 = input("What is your name?\n")
        name2 = input("what is thier name? \n")
        finName = name1 + name2
        f = finName.lower()
        first = f.count('t') + f.count('r') + f.count('u') + f.count('e')
        second = f.count('l') + f.count('o') + f.count('v') + f.count('e')
        score = str(first) + str(second)
        print(f"your love score is {score}")
