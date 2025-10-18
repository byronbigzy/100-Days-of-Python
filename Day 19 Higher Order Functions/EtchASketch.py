from turtle import Turtle, Screen

cursor = Turtle()
screen = Screen()

def move_forwards():
    cursor.forward(10)

def move_backwards():
    cursor.back(10)

def turn_left():
    new_heading = cursor.heading() + 10
    cursor.setheading(new_heading)

def turn_right():
    new_heading = cursor.heading() - 10
    cursor.setheading(new_heading)

def clear_drawing():
    screen.reset()

screen.listen()
screen.onkeypress(fun=move_forwards, key="w")
screen.onkeypress(fun=move_backwards, key="s")
screen.onkeypress(fun=turn_left, key="a")
screen.onkeypress(fun=turn_right, key="d")

screen.onkeypress(fun=clear_drawing, key="c")
screen.exitonclick()