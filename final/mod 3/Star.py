import turtle

# Create a turtle object
t = turtle.Turtle()

t.speed(1)

# Set the fill color to yellow
t.fillcolor("yellow")

# Begin filling the star with yellow color
t.begin_fill()

# Draw the star
for _ in range(5):
    t.forward(100)  # Move forward by 100 units
    t.right(144)    # Turn right by 144 degrees to form a point of the star

# End filling the star
t.end_fill()
t.heading()
t.position()
# Keep the window open
turtle.done()
