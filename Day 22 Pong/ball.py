from turtle import Turtle, mode
import random

mode("logo")

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.reset_position()

    def move(self):
        self.forward(5)

    def reset_position(self):
        self.goto(0,0)
        randranges = [random.randint(20, 70), random.randint(110, 160), random.randint(200, 250), random.randint(290, 340)]
        randint = random.choice(randranges)
        self.setheading(randint)
