from turtle import Turtle
import random

SCREEN_SIZE = 600
screen_min = int(SCREEN_SIZE/2)*-1
screen_max = int(SCREEN_SIZE/2)

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        random_x = random.randrange(start=screen_min+40, stop=screen_max-40, step=20)
        random_y = random.randrange(start=screen_min+40, stop=screen_max-40, step=20)
        self.goto(random_x, random_y)

    def respawn(self):
        random_x = random.randrange(start=screen_min+40, stop=screen_max-40, step=20)
        random_y = random.randrange(start=screen_min+40, stop=screen_max-40, step=20)
        self.goto(random_x, random_y)