from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.setheading(180)
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1,stretch_len=random.randint(1,5))
        self.goto(270,random.randint(-290,280))
    def move(self):
        new_x=self.xcor()-5
        self.goto(new_x,self.ycor())
    def gen(self):
        for i in range(0,random.randint(0,9)):
            self.penup()
            self.shape("square")
            self.setheading(180)
            self.color(random.choice(COLORS))
            self.shapesize(stretch_wid=1,stretch_len=random.randint(1,5))
            self.goto(270,random.randint(-290,280))

