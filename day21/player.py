from turtle import Turtle
STARTINGPOSITION=[(-280,0),(-280,20),(-280,40)]
STARTINGPOSITION2=[(280,0),(280,20),(280,40)]
up=10
down=10
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.pond=[]
        self.comp=[]
        
    def CreatePond(self):
        for pos in STARTINGPOSITION:
             segment=Turtle()
             segment.penup()
             segment.shape("square")
             segment.color("white")
             segment.goto(pos)
             segment.setheading(90)
             
             self.pond.append(segment)
        for pos in STARTINGPOSITION2:
             segment=Turtle()
             segment.penup()
             segment.shape("square")
             segment.color("white")
             segment.goto(pos)
             self.comp.append(segment)
   

    def up(self):
        self.pond[-1].setheading(90)
        for i in range(0,len(self.pond)-1):
            newx=self.pond[i+1].xcor()
            newy=self.pond[i+1].ycor()
            print(f"{newx} {newy}")
            self.pond[i].goto(newx,newy)
        self.pond[-1].forward(20)
    
        
    def compup(self):
        self.comp[-1].setheading(90)
        for i in range(0,len(self.comp)-1):
            newx=self.comp[i+1].xcor()
            newy=self.comp[i+1].ycor()
            print(f"{newx} {newy}")
            self.comp[i].goto(newx,newy)
        self.comp[-1].forward(20)
        
    def compdown(self):
        self.comp[0].setheading(270)
        for i in range(len(self.comp)-1,0,-1):
            newx=self.comp[i-1].xcor()
            newy=self.comp[i-1].ycor()
            self.comp[i].goto(newx,newy)
        self.comp[0].forward(20)
        
    def down(self):
        self.pond[0].setheading(270)
        for i in range(len(self.pond)-1,0,-1):
            newx=self.pond[i-1].xcor()
            newy=self.pond[i-1].ycor()
            self.pond[i].goto(newx,newy)
        self.pond[0].forward(20)


   
        

        
