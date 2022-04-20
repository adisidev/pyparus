import turtle
import math

# With inspiration from:
# https://www.geeksforgeeks.org/python-turtle-graphics-keyboard-commands/

# Initial setup
turtle.Screen()
turtle.bgcolor('black')
t = turtle.Turtle()
t.penup()
t.color('white')

# No delay
t.speed(0)

block_size = 50.0

# Movement functions
def set_heading_and_move(direction, distance = block_size):
    t.setheading(direction)
    t.fd(distance)

def get_dist(coord, direction = True):
    distance = (abs(coord) % block_size)
    if direction:
        distance = block_size - distance
    if distance == 0.0 or math.isclose(distance, 0.0, abs_tol = 1e-09) or math.isclose(distance, block_size):
        return block_size
    return distance


def up():
    distance = get_dist(t.pos()[1])
    set_heading_and_move(90.0, distance)
def down():
    distance = get_dist(t.pos()[1], False)
    set_heading_and_move(270.0, distance)
def right():
    distance = get_dist(t.pos()[0])
    set_heading_and_move(0.0, distance)
def left():
    distance = get_dist(t.pos()[0], False)
    set_heading_and_move(180.0, distance)

def toggle_pen():
    if t.isdown():
        t.penup()
    else:
        t.pendown()

next_x = True

def toggle_axis():

    # Swap axis
    global next_x
    next_x = not next_x

# Move toward perspective
def perspective(direction = True):

    # Draw till next integer axis value

    # Choose axis
    global next_x

    # X axis
    if next_x:
        f = math.cos

        # How much do we want to move to reach the next integer axis value
        movement = get_dist(t.pos()[0], direction)

    # Y axis
    else:
        f = math.sin
        movement = get_dist(t.pos()[1], direction)

    angle = t.towards(0.0, 0.0)
    distance = abs(movement / f(math.radians(angle)))
    if not direction:
        angle = angle - 180
    set_heading_and_move(angle, distance)

turtle.listen()

# Movement
turtle.onkey(up, 'w')
turtle.onkey(down, 's')
turtle.onkey(left, 'a')
turtle.onkey(right, 'd')

# Arrow keys
turtle.onkey(up, 'Up')
turtle.onkey(down, 'Down')
turtle.onkey(left, 'Left')
turtle.onkey(right, 'Right')

# Toggle axis
turtle.onkey(toggle_axis, 'l')

# Move to perspective point
turtle.onkey(perspective, 'j')

# Move away perspective point
turtle.onkey(lambda: perspective(False), 'k')

# Pen up/down
turtle.onkey(toggle_pen, 'p')
turtle.onkey(toggle_pen, 'f')

# Quit
turtle.onkey(turtle.bye, 'q')

# Undo
turtle.onkey(t.undo, 'u')

# Colors
# turtle.onkey(lambda: t.color('red'), 'r')
# turtle.onkey(lambda: t.color('green'), 'g')
# turtle.onkey(lambda: t.color('blue'), 'b')
# turtle.onkey(lambda: t.color('black'), 'r')

turtle.mainloop()
