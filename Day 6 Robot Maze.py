def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while True:
    if wall_on_right() and front_is_clear():
        move()
    if at_goal():
        break
    if front_is_clear():
        move()
    if not front_is_clear():
        turn_left()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
