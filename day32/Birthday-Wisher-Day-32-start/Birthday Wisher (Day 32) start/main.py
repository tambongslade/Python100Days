import smtplib

email = "tambongslade17@gmail.com"
Roshella="muyangroshella40@gmail.com"
password = "lydkfckhbqjhfryf"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(from_addr=email,
                        to_addrs=Roshella,
                        msg=f"Subject:Hello\n\nhello love\n i send it with python, i love you baby i need you Rn, but you aren't there")

import datetime as dt
import random
now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
dic={}
word= {}
if day_of_week==1:
    with open("quotes.txt",'r') as data:
        quotes = data.read()
        dic+=quotes.split("\n")
        word = random.choice(dic)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email,
                                to_addrs="email",
                                msg=f"Subject:Monday Motivation\n\n{word}")
