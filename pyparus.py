import turtle
import math

# With inspiration from:
# https://www.geeksforgeeks.org/python-turtle-graphics-keyboard-commands/

# Initial setup
turtle.Screen()
t = turtle.Turtle()

# No delay
t.speed(0)

block_size = 100.0

# Movement functions
def set_heading_and_move(direction, distance = block_size):
    t.setheading(direction)
    t.fd(distance)

def up(): set_heading_and_move(90.0)
def down(): set_heading_and_move(270.0)
def left(): set_heading_and_move(180.0)
def right(): set_heading_and_move(0.0)

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

# Quit
turtle.onkey(turtle.bye, 'q')

# Undo
turtle.onkey(lambda: turtle, 'u')

# Colors
# turtle.onkey(lambda: t.color('red'), 'r')
# turtle.onkey(lambda: t.color('green'), 'g')
# turtle.onkey(lambda: t.color('blue'), 'b')
# turtle.onkey(lambda: t.color('black'), 'r')

turtle.mainloop()
