from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]

class Snake:
    def __init__(self):
        self.body = []

        self.createSnake()

        self.head = self.body[0]

    def createSnake(self):
        for position in STARTING_POSITIONS:
            self.add_block(position)

    def add_block(self, position):
        block = Turtle(shape="square")
        block.penup()
        block.fillcolor("white")
        block.setpos(position)
        self.body.append(block)
        
    def extend(self):
        self.add_block(self.body[-1].position())
        
    def move(self):
        for block in range(len(self.body)-1, 0, -1):
            new_x = self.body[block - 1].xcor()
            new_y = self.body[block - 1].ycor()
            self.body[block].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() == 270:
            return
        self.head.setheading(90)

    def down(self):
        if self.head.heading() == 90:
            return
        self.head.setheading(270)

    def left(self):
        if self.head.heading() == 0:
            return
        self.head.setheading(180)

    def right(self):
        if self.head.heading() == 180:
            return
        self.head.setheading(0)
        