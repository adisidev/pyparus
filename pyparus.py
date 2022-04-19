import turtle
import math

# With inspiration from:
# https://www.geeksforgeeks.org/python-turtle-graphics-keyboard-commands/

# Initial setup
turtle.Screen()
t = turtle.Turtle()
t.penup()

# No delay
t.speed(0)

block_size = 100.0

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
    print(distance)
    set_heading_and_move(90.0, distance)
def down():
    distance = get_dist(t.pos()[1], False)
    print(distance)
    set_heading_and_move(270.0, distance)
def right():
    distance = get_dist(t.pos()[0])
    print(distance)
    set_heading_and_move(0.0, distance)
def left():
    distance = get_dist(t.pos()[0], False)
    print(distance)
    set_heading_and_move(180.0, distance)

def toggle():
    if t.isdown():
        t.penup()
    else:
        t.pendown()

# Move toward perspective
def perspective(direction = 1.0):
    angle = t.towards(0.0, 0.0)
    distance = abs(block_size / math.cos(math.radians(angle)))
    set_heading_and_move(angle, distance * direction)

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

# Move to perspective point
turtle.onkey(perspective, 'j')

# Move away perspective point
turtle.onkey(lambda: perspective(-1.0), 'k')

# Pen up/down
turtle.onkey(toggle, 'p')

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
