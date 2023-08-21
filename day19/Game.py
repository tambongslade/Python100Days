from turtle import Turtle,Screen
import random



colors=["red","orange","yellow","green","blue","purple"]
screen=Screen()
screen.setup(height=400,width=500)
is_race_on=False
user_bet=screen.textinput(title="make your bet", prompt="which turtle will win the race? Enter a color:")
print(user_bet)
position=[-70,-40,-10,20,50,80]
P=[]
for i in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(-230,position[i])
    P.append(new_turtle)

if user_bet:
    is_race_on=True
while is_race_on:
    for tur in P:
        if tur.xcor() > 230:
            winning=tur.pencolor()
            is_race_on=False
            if winning==user_bet:
                print(f"you won {winning} was the winner")
            else:
                print(f"you lose the winner was {winning} ")
        random_distance=random.randint(0,10)
        tur.forward(random_distance)
screen.exitonclick()