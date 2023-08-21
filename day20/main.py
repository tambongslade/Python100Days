from turtle import Turtle,Screen
from Snake import snake
import time
screen=Screen()
screen.bgcolor("black")
screen.setup(600,600)
screen.title("Snake Game")
sn=snake()
screen.listen()
screen.onkey(sn.up, "Up")
screen.onkey(sn.down, "Down")
screen.onkey(sn.left, "Left")
screen.onkey(sn.right, "Right")

screen.tracer(0)

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    sn.move()
screen.exitonclick()