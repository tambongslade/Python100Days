from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
       super().__init__()
       self.cars=[]
      
       for i in range(15):
            car=Turtle()
            car.shape("square")
            car.penup()
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1,stretch_len=3)
            car.goto(random.randint(-260,260),random.randint(-260,260))
            self.cars.append(car)
            self.Cposition=self.cars[0].xcor()+15
    def move(self):
        for car in self.cars:
            new_x=car.xcor()-STARTING_MOVE_DISTANCE
            car.goto(new_x,car.ycor())
    def gen(self):
            car=Turtle()
            car.shape("square")
            car.penup()
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1,stretch_len=3)
            car.goto(280,random.randint(-260,260))
            self.cars.append(car)
