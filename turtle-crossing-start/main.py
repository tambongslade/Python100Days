import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
jim=Player()
cars=CarManager()
cars.gen()
screen.listen()
screen.onkey(jim.up,"Up")
# screen.onkey(jim.down,"Down")
# screen.onkey(jim.right,"Right")
# screen.onkey(jim.left,"Left")
game_is_on = True
while game_is_on:
    cars.move()
    time.sleep(0.1)
    screen.update()
