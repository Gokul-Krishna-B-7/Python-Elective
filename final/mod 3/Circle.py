import turtle

t = turtle.Turtle()
t.pencolor("blue")
t.pensize(4)
t.circle(100)
t.up()
t.goto(0,-300)
t.down()
t.circle(150)
print(t.position())
turtle.done()