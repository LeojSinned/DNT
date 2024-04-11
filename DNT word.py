import turtle

# Initialize the turtle
t = turtle.Turtle()
turtle.setup(width=0.7, height=0.6)
# Set the turtle speed (adjust for desired speed)
t.speed(1)

# Set pen color (optional, change to desired color)
t.pencolor("black")


# Function to draw a straight line segment
def draw_line(length):
    t.forward(length)


# Function to draw a curve (optional, adjust for smoothness)
def draw_curve(radius, angle):
    t.circle(radius, angle)


# D
# Move turtle to starting position
t.penup()
t.goto(-100, 0)
t.pendown()

t.setheading(270)
draw_line(100)
t.left(90)
draw_curve(100, 180)
t.setheading(270)
draw_line(200)

# for letter N
t.penup()
t.goto(50, -100)
t.pendown()

t.setheading(270)
t.backward(200)
t.left(45)
t.forward(275)
t.right(45)
t.backward(200)

# for letter T
t.penup()
t.goto(300, 100)
t.pendown()

t.left(90)
t.forward(100)
draw_line(100)
t.backward(100)
t.right(90)
t.forward(200)
# Hide the turtle and keep the window open
t.hideturtle()
turtle.done()
