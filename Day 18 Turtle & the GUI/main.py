'''
import colorgram

colors = colorgram.extract('hirst_spot_painting.avif', 25)
rgb_colors = []

for color in colors:
    r = color.rgb[0]
    g = color.rgb[1]
    b = color.rgb[2]
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)
'''

import turtle
import random

colorList = [(208, 160, 82), (54, 89, 131), (146, 91, 40), (140, 26, 48), (222, 206, 108), (132, 177, 203), (158, 45, 83), (47, 55, 103), (167, 160, 38), (128, 189, 143), (84, 20, 44), (36, 42, 70), (187, 93, 105), (187, 139, 170), (84, 123, 181), (59, 39, 31), (78, 153, 165), (88, 157, 91), (195, 79, 72), (45, 74, 78), (161, 202, 220)]

turtle.colormode(255)

painter = turtle.Turtle()

# Inital Variables
painter.hideturtle()
painter.pencolor("")
painter.setpos(-350, -350)
origin = painter.pos()

number_of_dots = 100

for dot in range(1, number_of_dots + 1):
    position = painter.pos()
    color = random.choice(colorList)

    painter.dot(20, color)
    painter.setpos(position[0] + 50, position[1])

    if dot % 10 == 0:
        painter.setpos(position[0] - 450, position[1] + 50)

turtle.exitonclick()