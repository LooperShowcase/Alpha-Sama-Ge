import turtle

# Create a turtle object
t = turtle.Turtle()

# Set speed of the turtle
t.speed(0)

# Function to draw a circle
def draw_circle(radius):
    t.penup()
    t.goto(0, -radius)
    t.pendown()
    t.circle(radius)

# Set up the window
turtle.setup(width=600, height=600)

# Draw a perfect circle with radius 100
draw_circle(100)

# Keep the window open
turtle.done()