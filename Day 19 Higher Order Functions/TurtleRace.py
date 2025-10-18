from turtle import Turtle, Screen
import random

# Setup
screen = Screen()
screen.setup(width=400, height=400)

user_bet = screen.textinput(title="Place your bet!", prompt="Which turtle will win the race? Enter your color?")
is_racing = False

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

for i in range(0,6):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(colors[i])
    turtle.goto(x=-170, y=90-(i*30))
    all_turtles.append(turtle)

if user_bet:
    is_racing = True

while is_racing:
    for turtle in all_turtles:
        if turtle.xcor() >= 160:
            is_racing = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet.lower():
                print(f"You've won! The winner is the {turtle.pencolor()} turtle!")
            else:
                print(f"You've lost! The winner is the {turtle.pencolor()} turtle!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()