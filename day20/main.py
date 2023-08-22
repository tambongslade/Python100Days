from turtle import Screen
from Snake import snake
import time
from Food import food
from scoreboard import Scorebaord
screen=Screen()
screen.bgcolor("black")
screen.setup(600,600)
screen.title("Snake Game")
sn=snake()
Food=food()
score=Scorebaord()
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
    #detecting collision
    if sn.head.distance(Food)<15:
        Food.refresh()
        sn.extend()
        score.increment()
    
    if sn.head.xcor()> 280 or sn.head.xcor()<-280 or sn.head.ycor()<-280 or sn.head.ycor()>280:
        score.gameover()
        game_is_on=False
    #dectecting with tail
    for segment in sn.Snake[1:]:
        if sn.head.distance(segment)<10:
            game_is_on=False
            score.gameover()
screen.exitonclick()