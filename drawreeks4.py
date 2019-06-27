import turtle
stamp = turtle.Turtle()
stamp.shape("turtle")

stamp.penup()

for i in range (6):
    stamp.forward(50)
    stamp.stamp()
