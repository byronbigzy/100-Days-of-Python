import os
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
PATH = os.path.join(os.getcwd(), "Day 20-21 Snake", "highscore.txt")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(file=PATH, mode="r") as file:
            contents = file.read()
            self.highscore = int(contents)
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 300*0.8)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score >  self.highscore:
            self.highscore = self.score
            with open(file=PATH, mode="w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()