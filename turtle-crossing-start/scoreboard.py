from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.ht()
        self.goto(0,270)
        self.write(f"Score: {self.score}",align="center",font=FONT)
    def increase(self):
        self.score+=1
        self.clear()
        self.goto(0,270)
        self.write(f"Score: {self.score}",align="center",font=FONT)
    def gameOver(self):
        self.clear()
        self.goto(0,270)
        self.write("GameOver",align="center",font=FONT)
