from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()

SCREEN_WIDTH= 800
SCREEN_HEIGHT= 600
BACKGROUND_COLOR = "black"

screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(BACKGROUND_COLOR)
screen.title("Pong!")

screen.tracer(0)

right_paddle = Paddle(start_x=350)
left_paddle = Paddle(start_x=-350)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key="w", fun=left_paddle.move_up)
screen.onkeypress(key="s", fun=left_paddle.move_down)

screen.onkeypress(key="Up", fun=right_paddle.move_up)
screen.onkeypress(key="Down", fun=right_paddle.move_down)

# This can be fps
ball_speed = 1/60
running = True
while running:
    screen.update()
    ball.move()
    time.sleep(ball_speed)

    #Detect Wall Collision
    if ball.ycor() >= SCREEN_HEIGHT/2:
        if 270 < ball.heading() < 360:
            diff = ball.heading() - 270
            new_heading = 270 - diff
            ball.setheading(new_heading)

        if 0 < ball.heading() < 90:
            diff = 90 - ball.heading()
            new_heading = 90 + diff
            ball.setheading(new_heading)

    if ball.ycor() <= -SCREEN_HEIGHT/2:
        if 90 < ball.heading() < 180:
            diff = ball.heading() - 90
            new_heading = 90 - diff
            ball.setheading(new_heading)

        if 180 < ball.heading() < 270:
            diff = 270 - ball.heading()
            new_heading = 270 + diff
            ball.setheading(new_heading)

    # Detect Collision with Paddle:

    # Right Paddle
    if ball.distance(right_paddle) <= 50 and ball.xcor() >= 340:
        new_heading = ball.heading() + 180
        ball.setheading(new_heading)

    # Left Paddle
    if ball.distance(left_paddle) <= 50 and ball.xcor() <= -340:
        new_heading = ball.heading() - 180
        ball.setheading(new_heading)

    # Check Goal Collision

    # Right Goal
    if ball.xcor() >= 380:
        scoreboard.increase_P1_score()
        scoreboard.update_scoreboard()
        ball.reset_position()
        
    # Left Goal
    if ball.xcor() <= -380:
        scoreboard.increase_P2_score()
        scoreboard.update_scoreboard()
        ball.reset_position()

screen.exitonclick()

