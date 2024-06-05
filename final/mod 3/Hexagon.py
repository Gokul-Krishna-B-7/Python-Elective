import turtle

# Create a turtle object
t = turtle.Turtle()

t.speed(1)

# Set the fill color to green
t.fillcolor("green")

# Begin filling the hexagon with green color
t.begin_fill()

# Draw the hexagon
for _ in range(6):
    t.forward(100)  # Move forward by 100 units
    t.right(60)     # Turn right by 60 degrees to form a corner of the hexagon

# End filling the hexagon
t.end_fill()

# Keep the window open
turtle.done()
