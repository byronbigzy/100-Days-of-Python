from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.P1_score = 0
        self.P2_score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 300*0.8)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.P1_score}:{self.P2_score}", align=ALIGNMENT, font=FONT)

    def increase_P1_score(self):
        self.P1_score += 1
        self.update_scoreboard()
    
    def increase_P2_score(self):
        self.P2_score += 1
        self.update_scoreboard()