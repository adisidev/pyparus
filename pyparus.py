import turtle

# With inspiration from:
# https://www.geeksforgeeks.org/python-turtle-graphics-keyboard-commands/

# turtle.setup(500, 500)
turtle.Screen()
t = turtle.Turtle()
t.speed(0)
t.width(5)
# turtle.showturtle()


def up():
    t.setheading(90)
    t.forward(100)


def down():
    t.setheading(270)
    t.forward(100)


def left():
    t.setheading(180)
    t.forward(100)


def right():
    t.setheading(0)
    t.forward(100)


def r():
    t.color('red')


def g():
    t.color('green')

def u():
    t.undo()


def b():
    t.color('blue')


def z():
    t.color('black')

def q():
    turtle.bye()


turtle.listen()
turtle.onkey(up, 'Up')
turtle.onkey(down, 'Down')
turtle.onkey(left, 'Left')
turtle.onkey(right, 'Right')
turtle.onkey(z, 'z')

# Quit
turtle.onkey(q, 'q')

# Undo
turtle.onkey(u, 'u')

turtle.onkey(r, 'r')
turtle.onkey(g, 'g')
turtle.onkey(b, 'b')

turtle.mainloop()
