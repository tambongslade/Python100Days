import turtle as t
import random
t.colormode(255)
jimmy=t.Turtle()
jimmy.shape("classic")
jimmy.speed("fastest")
def genColor():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    radomColor=(r,g,b)
    return radomColor
 

directions=[180,90,0,270]
def drawSpiral(size_of_Gap):
    for _ in range(int(360/size_of_Gap)):
        jimmy.color(genColor())
        jimmy.circle(100)
        jimmy.setheading(jimmy.heading()+size_of_Gap)

drawSpiral(10)

    


        
    














screen=Screen()
screen.exitonclick()