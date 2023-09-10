##################### Extra Hard Starting Project ######################
import random
import smtplib

import pandas
# 1. Update the birthdays.csv
birthdays = pandas.read_csv("birthdays.csv")
birthdays = birthdays.to_dict(orient="records")
email = "tambongslade17@gmail.com"
password = "lydkfckhbqjhfryf"

# 2. Check if today matches a birthday in the birthdays.csv
import datetime as dt
date = dt.datetime.now().date()
for birth in birthdays:
    year = birth["year"]
    day = birth["day"]
    month = birth["month"]
    birthday= dt.datetime(year=year,day=day,month=month)
    print(birthday.date())
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    if date== birthday:
        with open(f"letter{random.randint(0,2)}.txt","r") as letter:
            l = letter.read()
            l = l.replace("[NAME]", birth["name"])
            print(l)
# 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("Smtp.google.com") as connection:
            connection.login(user=email,password=password)
            connection.starttls()
            connection.sendmail(to_addrs=birth["email"],
                                from_addr=email,
                                msg=l)




