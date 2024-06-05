import turtle
t=turtle.Turtle()
t.speed(1)
t.up()
t.goto(0,100)
t.down()
t.fillcolor("green")
t.begin_fill()
for i in range(8):
    t.forward(100)
    t.right(45)
t.end_fill()
t.hideturtle()
turtle.done()

import Grey