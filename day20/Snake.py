from turtle import Turtle
STARTINGPOSITION=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
up=90
down=270
left=180
right=0
class snake:
    def __init__(self) :
        self.Snake=[]
        self.create_snake()
        self.head=self.Snake[0]
    def create_snake(self):
        for pos in STARTINGPOSITION:
            self.addSegment(pos)
    def addSegment(self,pos):
            segment=Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(pos)
            self.Snake.append(segment)
    def extend(self):
        self.addSegment(self.Snake[-1].position())


    def move(self): 
            for segn in range(len(self.Snake)-1,0,-1):
                newx=self.Snake[segn-1].xcor()
                newy=self.Snake[segn-1].ycor()
                self.Snake[segn].goto(newx,newy)    
            self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading()!=down:
            self.head.setheading(90) 
    def down(self):
         if self.head.heading()!=up:
            self.head.setheading(270) 
    def left(self):
         if self.head.heading()!=right:
            self.head.setheading(180) 
    def right(self):
         if self.head.heading()!=left:
            self.head.setheading(0) 
  