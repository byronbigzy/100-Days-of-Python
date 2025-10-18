import turtle
import random
tim = turtle.Turtle()

'''
# Exercise 1: Draw a Square
for _ in range(4):
    tim.forward(100)
    tim.left(90)
'''

'''
# Exercies 2: Draw a Dashed Line
for _ in range(10):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
'''

turtle.colormode(255)

def randomColor():
    R = random.randint(0,225)
    G = random.randint(0,225)
    B = random.randint(0,225)
    tim.color(R,G,B)

# Exercise 3: Draw a triangle up to a decagon
'''
for i in range(3,11):
    total_degrees = (i-2) * 180
    print(f"Total Degrees: {total_degrees}")
    degrees_per_side = total_degrees / i
    print(f"Degrees per Side: {degrees_per_side}")
    randomColor()
    for j in range(1, i+1):
        tim.forward(100)
        tim.left(180-degrees_per_side)
'''

#Exercise 4: Random walk
'''
while True:
    randomColor()
    tim.forward(10)
    tim.setheading(random.choice([0, 90, 180, 270]))
'''

# Exercise 5: Draw a Spriograph
'''
tim.speed("fastest")
for i in range(0, 365, 5):
    randomColor()
    tim.circle(100)
    tim.setheading(i)
'''


turtle.exitonclick()