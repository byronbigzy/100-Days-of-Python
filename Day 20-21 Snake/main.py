import random

from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


'''
To Do:
Create a snake body [X]
Move the snake [X]
Control the snake [X]

Detect Collisions with Food
Scoreboard
Detect collison with wall
Detect collison with tail
'''

#Screen Setup
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GAME_SPEED = 0.1

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Setup Borders
border = Turtle()
border.color("white")
border.penup()
border.setpos(-280, -280)
border.pendown()
border.pensize(10)
border.forward(560)
border.left(90)
border.forward(560)
border.left(90)
border.forward(560)
border.left(90)
border.forward(560)
border.hideturtle()


running = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key="w", fun=snake.up)
screen.onkeypress(key="a", fun=snake.left)
screen.onkeypress(key="s", fun=snake.down)
screen.onkeypress(key="d", fun=snake.right)

while running:
    screen.update()
    time.sleep(GAME_SPEED)

    snake.move()

    # Check collison with food
    if snake.head.distance(food) < 10:
        food.respawn()
        snake.extend()
        scoreboard.increase_score()

    # Check collison with wall
    if snake.head.xcor() >= 280 or snake.head.xcor() <= -280 or snake.head.ycor() >= 270 or snake.head.ycor() <= -280:
        for block in snake.body:
            block.goto(5000, 5000)
        scoreboard.reset()
        snake.reset()


    # Check collision with tail
    for block in snake.body[1:]:
        if snake.head.distance(block) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()