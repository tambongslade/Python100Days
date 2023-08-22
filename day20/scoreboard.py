from turtle import Turtle
class Scorebaord(Turtle):
    def __init__(self) :
        super().__init__()
        self.score=0
        self.ht()
        self.speed("fastest")
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.show()
       
    def show(self):
        self.goto(0,280)
        self.write(f"Score: {self.score}",True,"center",("Arial",10,"bold"))
    def increment(self):
        self.clear()
              
        self.score+=1
        self.show()
    def gameover(self):
        self.goto(0,0)
        self.write(f"Game over",True,"center",("Arial",30,"bold"))
  
    


      