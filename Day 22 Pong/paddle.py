from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, start_x: int):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.setpos(x=start_x, y=0)

    def move_up(self):
        if self.ycor() == 260:
            return
        new_y = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_y)

    def move_down(self):
        if self.ycor() == -260:
            return 
        new_y = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_y)