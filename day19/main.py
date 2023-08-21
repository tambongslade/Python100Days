from turtle import Turtle, Screen
jimmy=Turtle()
screen=Screen()
def move():
    jimmy.forward(10)
def turn():
    turn=jimmy.heading()+10
    jimmy.setheading(turn)
def torn():
    turn=jimmy.heading()-10
    jimmy.setheading(turn)
def res():
    jimmy.clear()
    jimmy.penup()
    jimmy.goto(0,0)
    jimmy.pendown()
def back():
    jimmy.backward(10)
screen.listen()
 
screen.onkey(key="Up",fun=move)
screen.onkey(key="Left",fun=turn)
screen.onkey(key="Right",fun=torn)
screen.onkey(key="c",fun=res )
screen.onkey(key="Down",fun=back)
screen.exitonclick()