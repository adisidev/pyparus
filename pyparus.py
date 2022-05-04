import turtle
import math

# With inspiration from:
# https://www.geeksforgeeks.org/python-turtle-graphics-keyboard-commands/

# Initial setup
turtle.Screen()
turtle.bgcolor('white')
t = turtle.Turtle()
t.penup()
t.color('black')

# No delay
t.speed(0)

block_size = 50.0
step_size = block_size
vp = (0.0, 0.0)

# Movement functions
def set_heading_and_move(direction):
    t.setheading(direction)
    global step_size
    t.fd(step_size)

# Function to get distance
# def get_dist(coord, direction = True):
#     distance = (abs(coord) % block_size)
#     if direction:
#         distance = block_size - distance
#     if distance == 0.0 or math.isclose(distance, 0.0, abs_tol = 1e-09) or math.isclose(distance, block_size):
#         return block_size
#     return distance

def up():
    # distance = get_dist(t.pos()[1])
    set_heading_and_move(90.0) #, distance)
def down():
    # distance = get_dist(t.pos()[1], False)
    set_heading_and_move(270.0) #, distance)
def right():
    # distance = get_dist(t.pos()[0])
    set_heading_and_move(0.0) #, distance)
def left():
    # distance = get_dist(t.pos()[0], False)
    set_heading_and_move(180.0) #, distance)

def toggle_pen():
    if t.isdown():
        t.penup()
    else:
        t.pendown()

# next_x = True

# def toggle_axis():

#     # Swap axis
#     global next_x
#     next_x = not next_x


# Move toward perspective
def perspective(direction = True):

    # Draw till next integer axis value

    # Choose axis
    # global next_x

    # X axis
    # if next_x:
    #     f = math.cos

        # How much do we want to move to reach the next integer axis value
        # movement = get_dist(t.pos()[0], direction)

    # Y axis
    # else:
    #     f = math.sin
        # movement = get_dist(t.pos()[1], direction)

    angle = t.towards(vp)
    # distance = abs(movement / f(math.radians(angle)))
    if not direction:
        angle = angle - 180
    set_heading_and_move(angle) #, distance)

# Grid
grid = turtle.Turtle()
grid.color('grey')
grid.speed(0)
grid.hideturtle()

# Grid sizes
times = 12

# Perspective Grid
draw_pgrid = False

pgrid = turtle.Turtle()
pgrid.color('#808080')
pgrid.speed(0)
pgrid.pensize(2)
pgrid.hideturtle()

def toggle_pgrid(update_vp = False):
    global vp, draw_pgrid

    if update_vp:
        pgrid.clear()
        draw_pgrid = True

    if not update_vp:
        draw_pgrid = not draw_pgrid

    turtle.tracer(False)
    if draw_pgrid:
        r = range(-times, times)

        # Horizon line
        pgrid.color('#e74c3c')
        pgrid.penup()
        pgrid.goto(block_size * -times, vp[1])
        pgrid.pendown()
        pgrid.goto(block_size * +times, vp[1])

        # Vanishing point
        diameter = 10
        pgrid.penup()
        pgrid.goto(vp)
        pgrid.pendown()
        pgrid.dot(diameter, '#34495e')

    else:
        pgrid.clear()
    turtle.tracer(True)

def vp_up():
    global vp
    vp = (vp[0], vp[1] + block_size)
    toggle_pgrid(True)

def vp_down():
    global vp
    vp = (vp[0], vp[1] - block_size)
    toggle_pgrid(True)

def vp_left():
    global vp
    vp = (vp[0] - block_size, vp[1])
    toggle_pgrid(True)

def vp_right():
    global vp
    vp = (vp[0] + block_size, vp[1])
    toggle_pgrid(True)

# Square grid
draw_grid = False

# Draw one square
def square(trtl, size):
    for i in range(4):
        trtl.forward(size)
        trtl.left(90)

# Toggle square grid
def toggle_grid():
    global draw_grid
    draw_grid = not draw_grid
    turtle.tracer(False)
    r = range(-times, times)
    if draw_grid:
        for i in r:
            for j in r:
                grid.penup()
                grid.goto(i * block_size, j * block_size)
                grid.pendown()
                square(grid, block_size)
    else:
        grid.clear()
    turtle.tracer(True)
    if draw_pgrid:
        toggle_pgrid()
        toggle_pgrid()

step_sizes = [block_size, (block_size / 10.0)] #, (block_size / 20.0)]
size_selection = 0

def toggle_stepsize():
    global size_selection, step_sizes, step_size

    size_selection = (size_selection + 1) % len(step_sizes)
    step_size = step_sizes[size_selection]

# Interactivity
turtle.listen()

# Movement
turtle.onkey(up, 'w')
turtle.onkey(down, 's')
turtle.onkey(left, 'a')
turtle.onkey(right, 'd')
turtle.onkey(toggle_grid, 'g')

# Arrow keys
turtle.onkey(vp_up, 'Up')
turtle.onkey(vp_down, 'Down')
turtle.onkey(vp_right, 'Right')
turtle.onkey(vp_left, 'Left')
turtle.onkey(toggle_pgrid, ';')

# Toggle axis
turtle.onkey(toggle_stepsize, 'l')

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
turtle.onkey(t.undo, 'z')

# Colors
# turtle.onkey(lambda: t.color('red'), 'r')
# turtle.onkey(lambda: t.color('green'), 'g')
# turtle.onkey(lambda: t.color('blue'), 'b')
# turtle.onkey(lambda: t.color('black'), 'r')

turtle.mainloop()
