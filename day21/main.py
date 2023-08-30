from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen=Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("pong")
screen.tracer(0)
r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
score=Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"z")
screen.onkey(l_paddle.go_down,"s")

game_is_on=True
while game_is_on==True:
    time.sleep(ball.Move_speed)
    screen.update()
    ball.move()
    #detection ball with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bouncey()
    #detection of ball with paddle
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bouncex()

    #detect R padle misses
    if ball.xcor() > 380:
        ball.reset_position()
    
        score.l_point()
      
   
     #detect l padle misses
    if ball.xcor() < -380:
        ball.reset_position()
    
        score.r_point()

screen.exitonclick()