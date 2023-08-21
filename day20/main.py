from turtle import Turtle,Screen
import time
screen=Screen()
screen.bgcolor("black")
Snake=[]
position=[(0,0),(-20,0),(-40,0)]
screen.tracer(0)
is_snake=False
for pos in position:
    segment=Turtle("square")
    segment.color("white")

    segment.penup()
    segment.goto(pos)
    Snake.append(segment)
is_snake=True


while is_snake==True:
    screen.update()
    time.sleep(0.1)    

    for segn in range(len(Snake)-1,0,-1):
        newx=Snake[segn-1].xcor()
        newy=Snake[segn-1].ycor()
        Snake[segn].goto(newx,newy)
    Snake[0].forward(20)
    Snake[0].left(90)

    

screen.exitonclick()