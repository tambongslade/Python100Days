import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
score=Scoreboard()
jim=Player()
cars=CarManager()
screen.listen()
screen.onkey(jim.up,"Up")
# screen.onkey(jim.down,"Down")
# screen.onkey(jim.right,"Right")
# screen.onkey(jim.left,"Left")
game_is_on = True
counter=0
while game_is_on:
    cars.move()
    if counter==5:
        cars.gen()
        counter=0
    counter+=1
    #colision detextion between player and car
    for car in cars.cars:
        if car.distance(jim)<15:
            print("collision")
            jim.resetPosition()
            score.gameOver()
            game_is_on=False
    if jim.ycor()>230:
        cars.speed+=3
        jim.resetPosition()

        score.increase()
    time.sleep(0.1)
    
    screen.update()
screen.exitonclick()

