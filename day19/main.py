from turtle import Turtle, Screen
jimmy=Turtle()
screen=Screen()
def move():
    jimmy.forward(10)
screen.listen() 
screen.onkey(key="space",fun=move)
screen.exitonclick()