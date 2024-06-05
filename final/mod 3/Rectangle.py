import turtle

t = turtle.Turtle()


t.speed(1)


length = 300
breadth = 200

t.fillcolor("red")
t.begin_fill()

for _ in range(2):
    t.forward(length)  
    t.left(90)         
    t.forward(breadth) 
    t.left(90)         

t.end_fill()

turtle.done()
